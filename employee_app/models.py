from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave',   'Leave'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee} — {self.date} ({self.status})"


class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_records')
    month = models.DateField(help_text="Use the 1st day of month for grouping")
    rating = models.FloatField()
    goals_met = models.PositiveIntegerField()
    projects_completed = models.PositiveIntegerField(default=0)
    remarks = models.TextField(blank=True)

    class Meta:
        unique_together = ('employee', 'month')

    def __str__(self):
        return f"{self.employee} — {self.month:%Y-%m}"


class LeaveRecord(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('Sick',  'Sick Leave'),
        ('Casual','Casual Leave'),
        ('Earned','Earned Leave'),
    ]
    STATUS_CHOICES = [
        ('Pending',   'Pending'),
        ('Approved',  'Approved'),
        ('Rejected',  'Rejected'),
    ]

    employee= models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_records')
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    reason = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} — {self.leave_type} ({self.start_date} to {self.end_date})"

import random
from django.core.management.base import BaseCommand
from faker import Faker
from employee_app.models import Employee, Department, Attendance, Performance
from datetime import date, timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Generates synthetic employee data and saves it to the database'

    def handle(self, *args, **kwargs):
        # Ensure a department exists, if not, create one
        department = Department.objects.get_or_create(name="Engineering")[0]

        # Generate 4-5 employees with synthetic data
        for _ in range(5):
            employee = Employee.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                department=department,  # Link to existing department
                joining_date=fake.date_this_decade(),
                salary=random.randint(40000, 70000),
                position=fake.job(),
                phone_number=fake.phone_number()[:20],
                address=fake.address(),
                is_active=True
            )

            # Generate attendance records for this employee
            attendance_dates = set()
            while len(attendance_dates) < 10:
                attendance_dates.add(fake.date_this_year())

            for date_attended in attendance_dates:
                Attendance.objects.create(
                    employee=employee,
                    date=date_attended,
                    status=random.choice(['Present', 'Absent', 'Leave']),
                    check_in=fake.time(),
                    check_out=fake.time(),
                    notes=fake.sentence()
                )

            # Generate performance records for the employee
            performance_months = random.sample(range(1, 13), 5)  # 5 random months
            for month in performance_months:
                Performance.objects.create(
                    employee=employee,
                    month=date(2021, month, 1),  # Sample year, adjust as needed
                    rating=random.uniform(1.0, 5.0),
                    goals_met=random.randint(0, 5),
                    projects_completed=random.randint(0, 10),
                    remarks=fake.text(max_nb_chars=100)
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated synthetic employee data'))

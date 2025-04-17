from django.test import TestCase
from employee_app.models import Employee, Attendance, Performance, Department
from django.utils import timezone
from datetime import timedelta
from datetime import date


class EmployeeModelTest(TestCase):

    def test_create_employee(self):
        department = Department.objects.create(name="Engineering")
        employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            department=department,
            joining_date=timezone.now(),
            salary=50000.00,
            position="Software Engineer"
        )
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.department.name, "Engineering")

class AttendanceModelTest(TestCase):

    def test_create_attendance(self):
        dept = Department.objects.create(name="HR")
        employee = Employee.objects.create(first_name="John",last_name="Doe",
                                           joining_date=date(2021, 5, 10),
                                           salary=50000.00,
                                           email="john@example.com", department_id=dept.id)
        attendance = Attendance.objects.create(
            employee=employee,
            date=timezone.now(),
            status="Present"
        )
        self.assertEqual(attendance.employee.first_name, "John")
        self.assertEqual(attendance.status, "Present")

class PerformanceModelTest(TestCase):

    def test_create_performance(self):
        dept = Department.objects.create(name="HR")
        employee = Employee.objects.create(first_name="John",last_name="Doe",
                                           joining_date=date(2021, 5, 10),
                                           salary=50000.00,
                                           email="jane@example.com", department_id=dept.id)
        performance = Performance.objects.create(
            employee=employee,

            month=timezone.now().replace(day=1),
            rating=4.5,
            goals_met=3
        )
        self.assertEqual(performance.employee.first_name, "John")
        self.assertEqual(performance.rating, 4.5)

class DepartmentModelTest(TestCase):

    def test_create_department(self):
        department = Department.objects.create(name="HR")
        self.assertEqual(department.name, "HR")

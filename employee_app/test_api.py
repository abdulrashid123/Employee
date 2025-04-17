from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from employee_app.models import Employee, Department, Attendance, Performance
from datetime import date, timedelta


class EmployeeAPITestCase(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="HR")
        self.employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            department=self.department,
            joining_date=date.today() - timedelta(days=100),
            salary=50000,
            position="HR Manager"
        )

    def test_get_employees_list(self):
        url = reverse('employee-list')  # e.g., path name in urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("John", str(response.data))

    def test_employee_filter_by_department(self):
        url = reverse('employee-list') + f'?department={self.department.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_employee(self):
        url = reverse('employee-list')
        data = {
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com",
            "department": self.department.id,
            "department_id":self.department.id,
            "joining_date": date.today(),
            "salary": 60000,
            "position": "Recruiter"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)


class AttendanceAPITestCase(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="Engineering")
        self.employee = Employee.objects.create(
            first_name="Dev",
            last_name="Guy",
            email="dev@example.com",
            department=self.department,
            joining_date=date.today(),
            salary=75000,
            position="Engineer"
        )
        self.attendance = Attendance.objects.create(
            employee=self.employee,
            date=date.today(),
            status="Present"
        )

    def test_get_attendance_list(self):
        url = reverse('attendance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_attendance_detail(self):
        url = reverse('attendance-detail', args=[self.attendance.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PerformanceAPITestCase(APITestCase):

    def setUp(self):
        self.department = Department.objects.create(name="Sales")
        self.employee = Employee.objects.create(
            first_name="Sale",
            last_name="Man",
            email="sale@example.com",
            department=self.department,
            joining_date=date.today(),
            salary=67000,
            position="Sales Executive"
        )
        self.performance = Performance.objects.create(
            employee=self.employee,
            month=date.today().replace(day=1),
            rating=4.2,
            goals_met=3,
            projects_completed=1
        )

    def test_get_performance_list(self):
        url = reverse('performance-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_performance_rating_filter(self):
        url = reverse('performance-list') + '?rating__gte=4'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

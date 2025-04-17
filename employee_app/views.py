from rest_framework import generics, filters
from employee_app.models import Employee, Attendance, Performance, Department
from employee_app.serializers import (
    EmployeeSerializer,
    AttendanceSerializer,
    PerformanceSerializer,
    DepartmentSerializer
)
from django.db import transaction


# Department
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# Employee
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'position']
    ordering_fields = ['salary', 'joining_date']

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class EmployeeRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


# Attendance
class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AttendanceRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @transaction.atomic
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


# Performance
class PerformanceListCreateView(generics.ListCreateAPIView):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['employee__first_name']
    ordering_fields = ['rating', 'month']

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



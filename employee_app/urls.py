from django.urls import path
from employee_app.views import (
    DepartmentListCreateView,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateView,
    AttendanceListCreateView,
    PerformanceListCreateView,
    AttendanceRetrieveUpdateView,

)

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateView.as_view(), name='employee-detail'),
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-list'),
    path('attendance/<int:pk>/', AttendanceRetrieveUpdateView.as_view(), name='attendance-detail'),
    path('performance/', PerformanceListCreateView.as_view(), name='performance-list'),

]

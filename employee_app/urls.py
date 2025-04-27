from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendanceViewSet, PerformanceViewSet, DepartmentViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('attendances', AttendanceViewSet)
router.register('performances', PerformanceViewSet)
router.register('departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

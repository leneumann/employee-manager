from rest_framework.viewsets import ModelViewSet

from employees.api.serializers import EmployeeSerializer
from employees.models import Employee


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

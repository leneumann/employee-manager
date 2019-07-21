from rest_framework.viewsets import ModelViewSet

from employee.api.serializers import EmployeeSerializer
from employee.models import Employee


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

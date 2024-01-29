from rest_framework import serializers

from employee.model.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "username"]

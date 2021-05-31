from rest_framework import serializers
from adminapp.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_name', 'card_code', 'is_active', 'created_date', 'employee_rank', 'employee_games']
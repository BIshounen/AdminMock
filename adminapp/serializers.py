from rest_framework import serializers
from adminapp.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_games = serializers.CharField(source='get_employee_games_display')
    class Meta:

        model = Employee
        fields = '__all__'

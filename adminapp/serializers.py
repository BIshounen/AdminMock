from rest_framework import serializers, fields
from adminapp.models import Employee, GAMES


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_games = serializers.CharField(source='get_employee_games_display')
    class Meta:

        model = Employee
        fields = '__all__'

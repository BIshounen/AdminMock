from rest_framework import serializers, fields
from adminapp.models import Employee, GAMES


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_name']
        myField1 = fields.MultipleChoiceField(choices=GAMES)

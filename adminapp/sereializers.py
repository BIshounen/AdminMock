from rest_framework import serializers, fields
from adminapp.models import Employee, GAMES


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    myField1 = fields.MultipleChoiceField(choices=GAMES)

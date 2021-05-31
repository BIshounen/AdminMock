from rest_framework import serializers
from adminapp.models import Employee, Game


class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Game
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_games = GameSerializer(read_only=True, many=True)
    class Meta:

        model = Employee
        fields = '__all__'

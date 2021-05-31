from rest_framework import serializers
from adminapp.models import Employee, Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, value):
        return value.game_name

    class Meta:

        model = Game


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_games = GameSerializer(read_only=True, many=True)

    class Meta:

        model = Employee
        fields = '__all__'

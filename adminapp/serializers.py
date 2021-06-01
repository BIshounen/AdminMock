from rest_framework import serializers
from adminapp.models import Employee, Game


class GameSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        return value.game_name

    class Meta:

        model = Game
        fields = '__all__'


class GameSerializerFull(serializers.ModelSerializer):

    class Meta:

        model = Game
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    employee_games = GameSerializerFull(many=True, required=False)

    def create(self, validated_data):
        """
        Create and return a new `Employee` instance, given the validated data.
        """
        games = validated_data.pop('employee_games')
        employee = Employee.objects.create(**validated_data)
        for game in games:
            game_obj = Game.objects.get(pk=game['id'])
            employee.employee_games.add(game_obj)
        return employee

    def update(self, instance, validated_data):
        """
        Update and return an existing `Employee` instance, given the validated data.
        """
        instance.employee_name = validated_data.get('employee_name', instance.employee_name)
        instance.card_code = validated_data.get('card_code', instance.card_code)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.employee_rank = validated_data.get('employee_rank', instance.employee_rank)
        instance.employee_games = validated_data.get('employee_games', instance.employee_games)
        instance.save()
        return instance

    class Meta:

        model = Employee
        fields = '__all__'

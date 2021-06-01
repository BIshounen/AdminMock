from rest_framework import serializers
from adminapp.models import Employee, Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, value):
        return value.game_name

    class Meta:

        model = Game
        fields = '__all__'


class GameSerializerFull(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Game
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_games = GameSerializer(many=True, required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        games = validated_data.pop("employee_games")
        return str(games)

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

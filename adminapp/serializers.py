from rest_framework import serializers
from adminapp.models import Employee, Game
from django.contrib.auth.models import User


class GameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)
    class Meta:

        model = Game
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Employee` instance, given the validated data.
        """
        validated_data['email'] = "admin@admin.com"
        validated_data['is_superuser'] = True
        validated_data['is_staff'] = True

        user = User.objects.create(**validated_data)

        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing `Employee` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.employee_name)
        instance.set_password = validated_data.get('password', instance.password)
        instance.is_active = validated_data.get('is_active')

        return instance

    class Meta:

        model = User
        fields = ['id', 'username', 'is_active']


class EmployeeSerializer(serializers.ModelSerializer):
    employee_games = GameSerializer(many=True, required=False)

    def create(self, validated_data):
        """
        Create and return a new `Employee` instance, given the validated data.
        """
        games = validated_data.pop('employee_games')

        employee = Employee.objects.create(**validated_data)
        print(games)
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

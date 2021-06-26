from rest_framework import serializers
from adminapp.models import Employee, Game, GamePreset, RussianPokerSettings, RussianPokerBonusTable,\
    RouletteMinMax, RouletteSettings
from django.contrib.auth.models import User


class GameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)
    class Meta:

        model = Game
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(source='last_name', allow_blank=True, required=False)
    password = serializers.CharField(required=False, allow_blank=True, write_only=True)

    def create(self, validated_data):

        validated_data['email'] = "admin@admin.com"
        validated_data['is_superuser'] = True
        validated_data['is_staff'] = True
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        password = validated_data.get('password', "")
        if password != "":
            instance.set_password = password
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        return instance

    class Meta:

        model = User
        fields = ['id', 'username', 'is_active', 'comment', 'password', 'first_name']


class EmployeeSerializer(serializers.ModelSerializer):
    employee_games = GameSerializer(many=True, required=False)

    def create(self, validated_data):

        games = validated_data.pop('employee_games')

        employee = Employee.objects.create(**validated_data)
        print(games)
        for game in games:
            game_obj = Game.objects.get(pk=game['id'])
            employee.employee_games.add(game_obj)
        return employee

    def update(self, instance, validated_data):

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


class BonusTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RussianPokerBonusTable
        fields = '__all__'


class RPokerSettingsSerializer(serializers.ModelSerializer):

    bonus_table = BonusTableSerializer(many=True, read_only=True)

    class Meta:
        model = RussianPokerSettings
        fields = '__all__'


class RouletteMinMaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouletteMinMax
        fields = '__all__'


class RouletteSettingsSerializer(serializers.ModelSerializer):

    straight_up = RouletteMinMaxSerializer(many=False, read_only=True)

    class Meta:
        model = RouletteSettings
        fields = '__all__'


class PresetSerializer(serializers.ModelSerializer):
    game = serializers.SerializerMethodField(required=True, read_only=False)
    settings = serializers.SerializerMethodField(required=True, read_only=False)

    def get_game(self, instance):
        game = ""

        if hasattr(instance, 'russianpokersettings'):
            game = {'id': 1, 'name': 'Russian Poker'}
        return game

    def get_settings(self, instance):
        result = None
        if hasattr(instance, 'russianpokersettings'):
            result = RPokerSettingsSerializer(RussianPokerSettings.objects.get(pk=instance))
        elif hasattr(instance, 'roulettesettings'):
            result = RouletteSettingsSerializer(RouletteSettings.objects.get(pk=instance))

        return result.data

    def create(self, validated_data):
        print(validated_data)
        settings = validated_data.pop('settings')

        preset_object = GamePreset.objects.create(**validated_data)
        settings['preset'] = preset_object
        if validated_data['game']['id'] == 1:
            bonus_table = settings.pop('bonus_table')
            settings_object = RussianPokerSettings.objects.create(**settings)
            for bonus in bonus_table:
                bonus['settings'] = settings_object
                bonus_table_object = RussianPokerBonusTable.objects.create(**bonus)

        return preset_object

    class Meta:
        model = GamePreset
        fields = ['id', 'preset_name', 'partner', 'game', 'settings']

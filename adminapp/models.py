from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class Game(models.Model):
    game_name = models.CharField(max_length=255)

    def __str__(self):
        return self.game_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    card_code = models.IntegerField(blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    employee_rank = models.IntegerField(default=0)
    employee_games = models.ManyToManyField(Game, blank=True)

    def __str__(self):
        return self.employee_name


class GamePreset(models.Model):
    preset_name = models.CharField(max_length=255)
    preset_games = models.ForeignKey(Game, on_delete=models.CASCADE)


class RussianPokerSettings(models.Model):
    ante_min = models.IntegerField(default=0)
    bonus_min = models.IntegerField(default=0)
    payout_max = models.IntegerField(default=0)
    preset = models.OneToOneField(GamePreset, on_delete=models.CASCADE, primary_key=True)


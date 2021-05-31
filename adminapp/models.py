from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class Game(models.Model):
    game_name = models.CharField(max_length=200)

    def __str__(self):
        return self.game_name


class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    card_code = models.IntegerField(blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    employee_rank = models.IntegerField(default=0)
    employee_games = models.ManyToManyField(Game, blank=True)

    def __str__(self):
        return self.employee_name

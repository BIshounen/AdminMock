from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
GAMES = (
    (1, "Russian poker"),
    (2, "Baccarat"),
    (3, "Roulette"),
    (4, "Black Jack"),
)


class Employee(models.Model):
    employee_name = models.CharField(max_length=200)
    card_code = models.IntegerField(blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    employee_rank = models.IntegerField(default=0)
    employee_games = MultiSelectField(choices=GAMES, blank=True)

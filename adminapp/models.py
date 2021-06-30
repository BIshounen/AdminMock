from django.db import models
from django.core.exceptions import ObjectDoesNotExist
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


class Partner(models.Model):
    partner_name = models.CharField(max_length=255)
    one_wallet_cert = models.CharField(max_length=255)


class GamePreset(models.Model):
    preset_name = models.CharField(max_length=255)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.preset_name


class RussianPokerSettings(models.Model):
    ante_min = models.IntegerField(default=0)
    bonus_min = models.IntegerField(default=0)
    payout_max = models.IntegerField(default=0)
    preset = models.OneToOneField(GamePreset, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "for {}".format(str(self.preset))


class RussianPokerBonusTable(models.Model):
    lower_boundary = models.IntegerField(default=0)
    jackpot_percentage = models.IntegerField(default=0)
    settings = models.ForeignKey(RussianPokerSettings, on_delete=models.CASCADE, related_name='bonus_table')

    def __str__(self):
        return "{}-{} {}".format(self.lower_boundary, self.jackpot_percentage, str(self.settings))


class RouletteMinMax(models.Model):
    min = models.IntegerField(default=0)
    max = models.IntegerField(default=0)


class RouletteSettings(models.Model):
    preset = models.OneToOneField(GamePreset, on_delete=models.CASCADE, primary_key=True)
    straight_up = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="straight_up")
    split = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="split")
    street = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="street")
    corner = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="corner")
    six_line = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="six_line")
    column = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="column")
    dozen = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="dozen")
    even_chances = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="even_chances")
    voisins_de_zero = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="voisins_de_zero")
    zero_spiel = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="zero_spiel")
    orphelins = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="orphelins")
    series_5_8 = models.OneToOneField(RouletteMinMax, on_delete=models.CASCADE, related_name="series_5_8")

    def __str__(self):
        return "for {}".format(str(self.preset))

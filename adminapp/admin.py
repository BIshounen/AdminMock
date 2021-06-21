from django.contrib import admin
from adminapp.models import Employee, Game, GamePreset, RussianPokerSettings, RussianPokerBonusTable, RouletteSettings

# Register your models here.
admin.site.register(Employee)
admin.site.register(Game)
admin.site.register(GamePreset)
admin.site.register(RussianPokerSettings)
admin.site.register(RussianPokerBonusTable)
admin.site.register(RouletteSettings)

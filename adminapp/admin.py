from django.contrib import admin
from adminapp.models import Employee, Game, GamePreset

# Register your models here.
admin.site.register(Employee)
admin.site.register(Game)
admin.site.register(GamePreset)

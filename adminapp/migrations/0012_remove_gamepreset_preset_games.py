# Generated by Django 3.2.3 on 2021-06-18 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_auto_20210618_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamepreset',
            name='preset_games',
        ),
    ]

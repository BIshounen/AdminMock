# Generated by Django 3.2.3 on 2021-05-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_employee_employee_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_games',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_games',
            field=models.ManyToManyField(blank=True, to='adminapp.Game'),
        ),
    ]
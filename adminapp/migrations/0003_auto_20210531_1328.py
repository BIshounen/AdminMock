# Generated by Django 3.2.3 on 2021-05-31 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_employee_employee_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_games',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminapp.game'),
        ),
    ]

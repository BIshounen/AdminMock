# Generated by Django 3.2.3 on 2021-06-30 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0013_auto_20210621_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamepreset',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.partner'),
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-08 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0006_alter_game_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 1, 8, 16, 58, 15, 186364)
            ),
        ),
    ]

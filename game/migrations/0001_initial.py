# Generated by Django 4.1.5 on 2023-01-10 01:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 1, 9, 19, 50, 18, 291974)
                    ),
                ),
                ("phase", models.CharField(default="start_game", max_length=15)),
            ],
        ),
    ]

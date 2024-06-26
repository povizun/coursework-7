# Generated by Django 5.0.6 on 2024-06-26 22:33

import datetime

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
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
                    "destination",
                    models.CharField(
                        help_text="Укажите место выполнения привычки",
                        max_length=100,
                        verbose_name="Место выполнения",
                    ),
                ),
                (
                    "time_of_habit",
                    models.TimeField(
                        help_text="Укажите время, когда необходимо выполнять привычку",
                        verbose_name="Время выполнения",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        help_text="Укажите действие, которое представляет собой привычка",
                        max_length=100,
                        verbose_name="Действие привычки",
                    ),
                ),
                (
                    "period",
                    models.IntegerField(
                        choices=[
                            (1, "Каждый день"),
                            (2, "Каждые два дня"),
                            (3, "Каждые три дня"),
                            (4, "Каждые четыре дня"),
                            (5, "Каждые пять дней"),
                            (6, "Каждые шесть дней"),
                            (7, "Каждую неделю"),
                        ],
                        help_text="Укажите периодичность привычки",
                        verbose_name="Периодичность привычки",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        help_text="Укажите является ли данная привычка публичной",
                        verbose_name="Признак публичности",
                    ),
                ),
                (
                    "is_pleasant",
                    models.BooleanField(
                        help_text="Укажите является ли данная привычка полезной",
                        verbose_name="Признак приятной привычки",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        help_text="Укажите dознаграждение за выполнение привычки",
                        max_length=150,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(
                        default=datetime.timedelta(seconds=120),
                        help_text="Укажите время на выполнение привычки",
                        verbose_name="Время на выполнение (минуты)",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите создатель",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="создатель",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите связанную привычки",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habit_tracker.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычка",
                "ordering": ("pk",),
            },
        ),
    ]

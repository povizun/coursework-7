from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    class HabitPeriod(models.IntegerChoices):
        EVERY_DAY = 1, _("Каждый день")
        EVERY_2_DAYS = 2, _("Каждые два дня")
        EVERY_3_DAYS = 3, _("Каждые три дня")
        EVERY_4_DAYS = 4, _("Каждые четыре дня")
        EVERY_5_DAYS = 5, _("Каждые пять дней")
        EVERY_6_DAYS = 6, _("Каждые шесть дней")
        EVERY_WEEK = 7, _("Каждую неделю")

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="создатель",
        help_text="Укажите создатель",
    )
    destination = models.CharField(
        max_length=100,
        verbose_name="Место выполнения",
        help_text="Укажите место выполнения привычки",
    )
    time_of_habit = models.TimeField(
        verbose_name="Время выполнения",
        help_text="Укажите время, когда необходимо выполнять привычку",
    )
    action = models.CharField(
        max_length=100,
        verbose_name="Действие привычки",
        help_text="Укажите действие, которое представляет собой привычка",
    )
    period = models.IntegerField(
        choices=HabitPeriod.choices,
        verbose_name="Периодичность привычки",
        help_text="Укажите периодичность привычки",
    )
    is_public = models.BooleanField(
        verbose_name="Признак публичности",
        help_text="Укажите является ли данная привычка публичной",
    )
    is_pleasant = models.BooleanField(
        verbose_name="Признак приятной привычки",
        help_text="Укажите является ли данная привычка полезной",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычки",
    )
    reward = models.CharField(
        max_length=150,
        verbose_name="Вознаграждение",
        help_text="Укажите dознаграждение за выполнение привычки",
    )
    duration = models.DurationField(
        default=timedelta(minutes=2),
        verbose_name="Время на выполнение (минуты)",
        help_text="Укажите время на выполнение привычки",
    )

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычка"
        ordering = ("pk",)

from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habit_tracker.services import send_telegram_message

from habit_tracker.models import Habit


@shared_task
def send_alert():
    """Функция оповещения о полезной привычке"""
    current_datetime = timezone.now().today().replace(second=0, microsecond=0)
    missed_habits = Habit.objects.filter(is_plesant=False).filter(time_of_habit__lt=current_datetime)
    for habit in missed_habits:
        while habit.time_of_habit < current_datetime:
            habit.time_of_habit = habit.time_of_habit + timedelta(days=habit.period)
        habit.save()
    habits = Habit.objects.filter(is_plesant=False).filter(time_of_habit=current_datetime)
    for habit in habits:
        message_1 = f"Полезная привычка: {habit}"
        if habit.related_habit:
            message_2 = f"За выполнение Вы можете: {habit.related_habit}"
        elif habit.reward:
            message_3 = f"За выполнение Вам можно: {habit.reward}"

        if habit.owner.telegram_id:
            send_telegram_message(
                telegram_id=habit.owner.telegram_id,
                message=message_1,
            )
            if habit.related_habit:
                send_telegram_message(
                    telegram_id=habit.owner.telegram_id,
                    message=message_2,
                )
            elif habit.reward:
                send_telegram_message(
                    telegram_id=habit.owner.telegram_id,
                    message=message_3,
                )
        habit.time_of_habit = habit.time_of_habit + timedelta(days=habit.period)
        habit.save()

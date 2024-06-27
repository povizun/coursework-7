from datetime import timedelta

from rest_framework import serializers


class MultiplyChoiceHabitValidator:

    def __init__(self, reward, related_habit):
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        if value.get(self.reward) == value.get(self.related_habit):
            raise serializers.ValidationError(
                "У полезной привычки не может быть вознаграждения"
                " и связанной привычки одновременно"
            )


class DurationValidator:

    def __call__(self, value):
        if value:
            if value > timedelta(minutes=2):
                raise serializers.ValidationError(
                    "Время на выполнение привычки не должно превышать 120 секунд"
                )


class RelatedHabitValidator:

    def __init__(self, related_habit):
        self.related_habit = related_habit

    def __call__(self, value):
        if value.get(self.related_habit):
            if not value.get(self.related_habit).is_plesant:
                raise serializers.ValidationError(
                    "В связанные привычки могут попадать только привычки"
                    'с признаком "приятной" привычки'
                )


class PleasantHabitValidator:

    def __init__(self, is_pleasant, reward, related_habit):
        self.is_pleasant = is_pleasant
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        if value.get(self.is_pleasant) and (
            value.get(self.reward) or value.get(self.related_habit)
        ):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения"
                "или связанной привычки"
            )

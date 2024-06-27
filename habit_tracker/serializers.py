from rest_framework import serializers

from habit_tracker.models import Habit
from habit_tracker.validators import (DurationValidator,
                                      MultiplyChoiceHabitValidator,
                                      PleasantHabitValidator,
                                      RelatedHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    duration = serializers.DurationField(validators=[DurationValidator()])

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            MultiplyChoiceHabitValidator(
                reward="reward", related_habit="related_habit"
            ),
            RelatedHabitValidator(related_habit="related_habit"),
            PleasantHabitValidator(
                is_pleasant="is_pleasant",
                reward="reward",
                related_habit="related_habit",
            ),
        ]

from django.urls import path

from habit_tracker.apps import HabitTrackerConfig
from habit_tracker.views import (HabitCreateAPIView, HabitDestroyAPIView,
                                 HabitRetrieveAPIView, HabitUpdateAPIView,
                                 PublicHabitsListAPIView,
                                 UserHabitsListAPIView)

app_name = HabitTrackerConfig.name

urlpatterns = [
    path("habits/", PublicHabitsListAPIView.as_view(), name="public_habits_list"),
    path("habits/my/", UserHabitsListAPIView.as_view(), name="user_habits_list"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="create_habit"),
    path("habits/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="update_habit"),
    path("habits/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="delete_habit"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="detail_habit"),
]

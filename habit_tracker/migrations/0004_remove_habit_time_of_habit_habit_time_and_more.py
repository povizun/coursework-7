# Generated by Django 5.0.6 on 2024-06-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "habit_tracker",
            "0003_alter_habit_is_pleasant_alter_habit_is_public_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="time_of_habit",
        ),
        migrations.AddField(
            model_name="habit",
            name="time",
            field=models.DateTimeField(
                auto_now=True,
                help_text="Укажите дату и время, когда необходимо выполнить привычку",
                verbose_name="Время следующего выполнения",
            ),
        ),
        migrations.AlterField(
            model_name="habit",
            name="reward",
            field=models.CharField(
                help_text="Укажите вознаграждение за выполнение привычки",
                max_length=150,
                verbose_name="Вознаграждение",
            ),
        ),
    ]

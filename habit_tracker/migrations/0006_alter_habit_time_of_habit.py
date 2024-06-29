# Generated by Django 5.0.6 on 2024-06-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit_tracker", "0005_rename_time_habit_time_of_habit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time_of_habit",
            field=models.DateTimeField(
                help_text="Укажите дату и время, когда необходимо выполнить привычку",
                verbose_name="Время следующего выполнения",
            ),
        ),
    ]

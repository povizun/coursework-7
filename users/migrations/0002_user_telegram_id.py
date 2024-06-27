# Generated by Django 5.0.6 on 2024-06-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="telegram_id",
            field=models.CharField(
                default=0,
                help_text="Укажите ваш chat-ID в телеграмм",
                max_length=50,
                unique=True,
                verbose_name="Chat-ID в телеграмм",
            ),
            preserve_default=False,
        ),
    ]

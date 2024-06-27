import requests
from config import settings


def send_telegram_message(telegram_id, message):
    """Функция отправки уведомления в Telegram"""
    params = {
        'chat_id': telegram_id,
        'text': message,
    }
    requests.post(
        f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage',
        params=params
    )

from aiogram import Bot
from core.config import settings
from core.scheduler import scheduler
from core.tg_bot import bot
from utils.request import do_request


async def send_daily_statistics_notification(bot: Bot, user_id: int, hour: int, minute: int):
    async with do_request(
            url=f'{settings.BOT_BACKEND_HOST}/stats',
            params={'period': 'day'},
            headers={'user_from_id': str(user_id), 'Authorization': f'Bearer {settings.AUTH_KEY}'},
            method='GET'
    ) as response:
        if response.status == 200:
            stats = await response.json()
            await bot.send_message(
                user_id, f"Your daily statistics:\nTotal calories: {stats['total']}\nDaily average: {stats['daily_average']}"
            )
        else:
            print('An error occurred while fetching daily statistics.')


async def schedule_daily_notifications():
    async with do_request(
            url=f'{settings.BOT_BACKEND_HOST}/user/chats',
            headers={'Authorization': f'Bearer {settings.AUTH_KEY}'},
            method='GET'
    ) as response:
        if response.status == 200:
            users = await response.json()
            for user in users['items']:
                user_id = user['user_id']
                hour = user.get('notification_hour', 9)  # Default hour
                minute = user.get('notification_minute', 0)  # Default minute
                scheduler.add_job(
                    send_daily_statistics_notification,
                    trigger='cron',
                    hour=hour,
                    minute=minute,
                    kwargs={'bot': bot, 'user_id': user_id, 'hour': hour, 'minute': minute}
                )
        else:
            print('Failed to fetch user data for scheduling notifications.')


scheduler.add_job(
    schedule_daily_notifications,
    trigger='cron',
    hour=0,  # Начать проверку и планирование уведомлений в полночь
    minute=0,
)


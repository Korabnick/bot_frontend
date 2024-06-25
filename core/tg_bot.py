import asyncio

from aiogram import Bot, F
from aiogram import Dispatcher, types
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand

from core.buttons import get_main_keyboard
from core.config import settings
from core.logger import setup_logger
from core.redis_connection import redis
from core.scheduler import scheduler
from handlers.base_functional.router import base_router
from handlers.notifications.router import notification_router
from handlers.calories.router import calories_router
from middleware.logger import LogMessageMiddleware


bot = Bot(token=settings.BOT_TOKEN)
storage = RedisStorage(redis)
dp = Dispatcher(storage=storage, bot=bot)


def get_dispatcher() -> Dispatcher:
    global dp

    return dp


def get_tg_bot() -> Bot:
    global bot

    return bot


async def main():
    await bot.delete_webhook()
    dp.include_router(calories_router)
    dp.include_router(base_router)
    dp.include_router(notification_router)

    setup_logger()

    dp.message.middleware(LogMessageMiddleware())
    dp.callback_query.middleware(LogMessageMiddleware())

    await bot.set_my_commands(
        [
            BotCommand(command='start', description='Start bot')
        ]
    )
    await dp.start_polling(bot)


@dp.message(F.text == '/start')
async def start_message(message: types.Message):
    await message.answer(
        'Hi! I\'ll help you keep track of your calories.',
        reply_markup=get_main_keyboard(),
    )


async def start_scheduler():
    scheduler.start()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.create_task(main())
    loop.create_task(start_scheduler())
    loop.run_forever()

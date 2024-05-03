import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from .handlers import router

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(router)


async def set_default_commands():
    await bot.set_my_commands([
        BotCommand(command='add', description='Создать задачу'),
        BotCommand(command='tsk', description='Вывести список задач'),
    ])

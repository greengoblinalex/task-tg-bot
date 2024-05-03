import asyncio

from src.database import create_all
from src.bot import dp, bot, set_default_commands


async def main():
    await create_all()
    await set_default_commands()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

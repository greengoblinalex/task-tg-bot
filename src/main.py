import asyncio

from src.database import create_all
from src.bot import dp, bot, set_default_commands


async def main():
    await create_all()
    await set_default_commands()
    print('Bot enabled')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot disabled')

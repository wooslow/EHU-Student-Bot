import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from routers import welcome_router

load_dotenv()


async def main():
    bot = Bot(
        token=os.getenv('TELEGRAM_TOKEN'),
        default=DefaultBotProperties(
            parse_mode="HTML"
        )
    )
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(welcome_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

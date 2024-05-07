import asyncio
import os

from aiogram import Bot
from dotenv import load_dotenv

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    print("Started....")
    from handlers import dp
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

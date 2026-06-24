import os
import asyncio
from dotenv import load_dotenv
from telegram import Bot


async def main():
    load_dotenv()

    bot_token = os.getenv("BOT_TOKEN")
    telegram_id = os.getenv("TELEGRAM_ID")

    if not bot_token:
        raise ValueError("BOT_TOKEN не найден в файле .env")

    if not telegram_id:
        raise ValueError("TELEGRAM_ID не найден в файле .env")

    bot = Bot(token=bot_token)

    await bot.send_message(

    chat_id=telegram_id,

    text="Привет, Евгений! TravelHunter запущен 🚀",

    connect_timeout=30,

    read_timeout=30

)

    print("Сообщение отправлено в Telegram")


if __name__ == "__main__":
    asyncio.run(main())
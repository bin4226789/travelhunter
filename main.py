import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from cities import AUSTRALIA

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, Евгений!\n\n"
        "TravelHunter работает.\n\n"
        "Доступные команды:\n"
        "/start\n"
        "/cheap"
    )


async def cheap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "TravelHunter проверяет направления:\n\n"

    for code, city in AUSTRALIA.items():
        text += f"✈️ {city} ({code})\n"

    await update.message.reply_text(text)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cheap", cheap))

    print("TravelHunter запущен")

    app.run_polling()


if __name__ == "__main__":
    main()
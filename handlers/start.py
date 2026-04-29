from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Get Started"],
        ["Services"],
        ["Contact Admin"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Welcome to my Lead Generation Bot! 🚀\n\n"
        "Choose an option below:",
        reply_markup=reply_markup
    )

start_handler = CommandHandler("start", start)

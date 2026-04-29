from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Import command handler from handlers folder
from handlers.start import start_handler

# Replace with your actual bot token
BOT_TOKEN = "8585594114:AAHwDuRtq1fyhNa_ntNF0-9NNMyI7EliTEA"


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Get Started":
        await update.message.reply_text(
            "🚀 Welcome! I help businesses generate high-quality leads and grow faster.\n\n"
            "Use the menu below to explore our services or contact support."
        )

    elif text == "Services":
        await update.message.reply_text(
            "🛠 Our Services:\n\n"
            "• Lead Generation\n"
            "• Email Marketing\n"
            "• Shopify Store Development\n"
            "• Sales Funnel Setup\n"
            "• Business Growth Strategy"
        )

    elif text == "Contact Admin":
        await update.message.reply_text(
            "📩 Contact Admin:\n"
            "@Gupcupp\n\n"
            "We typically respond as quickly as possible."
        )

    else:
        await update.message.reply_text(
            "Please choose an option from the menu below."
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    app.add_handler(start_handler)

    # Button handler
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons)
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()

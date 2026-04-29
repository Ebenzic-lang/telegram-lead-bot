from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from handlers.start import start_handler

BOT_TOKEN = "8585594114:AAHwDuRtq1fyhNa_ntNF0-9NNMyI7EliTEA"


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "Get Started":
        await update.message.reply_text(
            "🚀 Welcome! I'm here to help you generate and manage leads efficiently."
        )

    elif text == "Services":
        await update.message.reply_text(
            "🛠 Our Services:\n\n"
            "• Lead Generation\n"
            "• Email Marketing\n"
            "• Shopify Store Setup\n"
            "• Sales Funnel Creation"
        )

    elif text == "Contact Admin":
        await update.message.reply_text(
            "📩 Contact Admin:\n@Gupcupp"
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(start_handler)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()

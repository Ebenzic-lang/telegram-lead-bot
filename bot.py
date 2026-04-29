from telegram.ext import Application, CommandHandler
from handlers.start import start_handler

# Replace with your real Telegram bot token
BOT_TOKEN = "8585594114:AAHwDuRtq1fyhNa_ntNF0-9NNMyI7EliTEA"


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    app.add_handler(start_handler)

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()

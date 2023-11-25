from telegram.ext import ApplicationBuilder
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.run_polling()


if __name__ == '__main__':
    main()

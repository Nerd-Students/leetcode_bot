#!/usr/bin/env python

from dotenv.main import os
from telegram import ForceReply, Update
import multiprocessing
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf'Привет, {user.mention_html()}!',
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Памагити!')


def poll() -> None:
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


def schedule() -> None:
    raise NotImplementedError


def main() -> None:
    """Бот делится на две части.

    poller_process - парсит сообщения пользователей.
    scheduler_process - запускает сообщения по расписанию.
    """
    poller_process = multiprocessing.Process(name='tg_bot_poll', target=poll)
    scheduler_process = multiprocessing.Process(
        name='tg_bot_schedule', target=schedule
    )
    poller_process.start()
    scheduler_process.start()


if __name__ == '__main__':
    main()

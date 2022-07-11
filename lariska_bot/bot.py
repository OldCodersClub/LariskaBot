import logging

from aiogram.utils.executor import start_webhook

from lariska_bot.config import (
    WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
)
from lariska_bot.dispatcher import bot, dp
import lariska_bot.handlers


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


def main():
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

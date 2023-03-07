from aiogram.utils.executor import start_webhook

from lariska_bot.config import (
    WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT
)
from lariska_bot.dispatcher import bot
from lariska_bot.handlers.handler import *


# noinspection PyUnusedLocal
async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


# noinspection PyUnusedLocal
async def on_shutdown(dispatcher):
    pass
    # await bot.delete_webhook()


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Restart and run server.')
    logging.info(f'Local datetime: {datetime.now()}')
    logging.info(
        f"Moscow datetime: {datetime.now(pytz.timezone('Europe/Moscow'))}"
    )

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )


if __name__ == '__main__':
    main()

import logging
from pathlib import Path

from aiogram.utils.executor import start_polling

from lariska_bot.handlers.handler import *


def main():
    log_name = f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    Path(log_name).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        filename=log_name,
        filemode="a"
    )

    start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()

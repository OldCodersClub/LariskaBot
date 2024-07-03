import logging
import sys

from aiogram import Bot,Dispatcher
from aiogram.client.default import DefaultBotProperties
from config_data.config import Config, load_config
from handlers.handler import router

logger = logging.getLogger(__name__)
dp = Dispatcher()

if __name__ == '__main__':

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.debug('Путь sys.path:')
    logger.debug(sys.path)
    logger.debug('Встроенные модули sys.builtin_module_names:')
    logger.debug(sys.builtin_module_names)
    logger.debug('Модули из стандартной библиотеки Python sys.stdlib_module_names:')
    logger.debug(sys.stdlib_module_names)

    # Загружаем конфиг в переменную config
    config: Config = load_config()
    logger.debug(config)

    # Инициализируем бот и диспетчер
    logger.debug('Инициализируем бот')
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode='HTML'))
    logger.debug('Бот инициализирован')

    logger.info('Запуск бота')
    logger.debug('Запускаем диспетчер')

    # Регистрируем роутер из модуля handlers
    dp.include_router(router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    bot.delete_webhook(drop_pending_updates=True) # Перезапускаем диспетчер
    dp.run_polling(bot)
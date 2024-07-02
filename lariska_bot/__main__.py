import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import Config, load_config
from handlers import handler
from create_dp import dp


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    storage = MemoryStorage()
    # dp = Dispatcher() # Подготовка диспетчера

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

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
    dp.include_router(handler.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    bot.delete_webhook(drop_pending_updates=True) # Перезапускаем диспетчер
    dp.run_polling(bot)
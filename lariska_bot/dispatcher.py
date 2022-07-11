from aiogram import Bot, Dispatcher

from lariska_bot.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

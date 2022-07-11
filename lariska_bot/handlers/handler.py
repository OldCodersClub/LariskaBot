from aiogram import types
from aiogram.dispatcher.filters import Text

from lariska_bot.dispatcher import dp


@dp.message_handler(Text(contains=['лариска', 'дура'], ignore_case=True))
async def himself_like_this(message: types.Message):
    await message.reply('Сам такой!')

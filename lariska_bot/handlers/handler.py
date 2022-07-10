from aiogram import types

from lariska_bot.bot import dp


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

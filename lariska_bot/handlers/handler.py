import logging
from datetime import datetime, timedelta
from random import choice

import pytz
from aiogram import types
from aiogram.dispatcher.filters import Text
from ruamel import yaml

from lariska_bot.dispatcher import dp
from lariska_bot.handlers.answers import get_answer
from lariska_bot.handlers.users import users


MESSAGES = {
    x: y.replace(r'\n', '\n') for (x, y)
    in yaml.load(open('/app/lariska_bot/handlers/messages.yaml'),
                 Loader=yaml.Loader).items()
}

REPLICAS = {
    x: [z.replace(r'\n', '\n') for z in y] for (x, y)
    in yaml.load(open('/app/lariska_bot/handlers/replicas.yaml'),
                 Loader=yaml.Loader).items()
}


# noinspection PyUnusedLocal
async def flood_controlling(*args, **kwargs):
    await args[0].reply(MESSAGES['flood_reply'])


@dp.message_handler(Text(contains=['говно'], ignore_case=True))
async def skirmish_reply(message: types.Message):
    await message.reply(MESSAGES['skirmish'])


@dp.message_handler(Text(contains=['привет', 'с чего начать'], ignore_case=True))
async def hello_where_to_reply(message: types.Message):
    await message.reply(MESSAGES['hello'])
    await message.answer(MESSAGES['start_here'])
    await message.answer(MESSAGES['start_video'])
    await message.answer(MESSAGES['message_links'])


@dp.message_handler(Text(contains=['привет'], ignore_case=True))
async def hello_reply(message: types.Message):
    await message.reply(MESSAGES['hello'])


@dp.message_handler(Text(contains=['с чего начать'], ignore_case=True))
async def where_to_begin(message: types.Message):
    await message.reply(MESSAGES['start_here'])
    await message.answer(MESSAGES['start_video'])
    await message.answer(MESSAGES['message_links'])


@dp.message_handler(Text(contains=['лариска', 'бот'], ignore_case=True))
async def lariska_bot_reply(message: types.Message):
    await message.reply(MESSAGES['lariska_bot'])
    await message.answer(MESSAGES['forks'])


@dp.message_handler(Text(contains=['https://t.me/oldcoders_bar'], ignore_case=True))
async def bar_reply(message: types.Message):
    await message.reply(choice(REPLICAS['bar']))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        MESSAGES['welcome'], parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
@dp.throttled(flood_controlling, rate=5)
async def text_reply(message: types.Message):
    username = message.from_user.username
    user_dict = users.get(username)

    tz = pytz.timezone('Europe/Moscow')
    present_date = datetime.now(tz)
    present_date += timedelta(hours=5)
    present_day = present_date.day

    if user_dict and user_dict['day'] != present_day:
        user_dict['day'] = present_day
        await message.reply(choice(user_dict['greetings']))

    else:
        answer, rating, = get_answer(message.text)
        logging.info(f'{rating}:{answer}')  # WTF: debug logging
        if rating >= 90:
            await message.reply(f'{answer}')


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_reply(message: types.Message):
    await message.reply(MESSAGES['photo_reply'])

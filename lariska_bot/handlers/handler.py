from datetime import datetime, timedelta
from random import choice

import pytz
from aiogram import types
from aiogram.dispatcher.filters import Text

from lariska_bot import (MESSAGES, REPLICAS, USERS, WORKS_CHATS,
                         BOT_FIRST_NAME, RATING_LIMIT, FLOOD_RATE, L_USERS)
from lariska_bot.dispatcher import dp
from lariska_bot.handlers.controllers import (flood_controlling, get_answer,
                                              get_ai_answer)


@dp.message_handler(Text(contains=['говно'], ignore_case=True))
async def skirmish_reply(message: types.Message):
    await message.reply(MESSAGES['skirmish'])


@dp.message_handler(Text(contains=['привет', 'с чего начать'],
                         ignore_case=True))
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


@dp.message_handler(Text(contains=['https://t.me/oldcoders_bar'],
                         ignore_case=True))
async def bar_reply(message: types.Message):
    await message.reply(choice(REPLICAS['bar']))


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        MESSAGES['welcome'], parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
@dp.throttled(flood_controlling, rate=FLOOD_RATE)
async def text_reply(message: types.Message):
    username = message.from_user.username
    user_day = USERS.get(username)

    tz = pytz.timezone('Europe/Moscow')
    present_date = datetime.now(tz)

    current_date = present_date - timedelta(hours=5)
    current_day = current_date.day

    if username in USERS and user_day != current_day:
        USERS[username] = current_day
        await message.reply(choice(REPLICAS[username]))
        return

    answer, rating, = get_answer(message.text)

    if rating >= RATING_LIMIT:
        await message.reply(f'{answer}')
        return

    # AI
    if message.text.startswith(BOT_FIRST_NAME):
        if str(message.chat.id) in WORKS_CHATS:
            if username in L_USERS:
                await message.reply(choice(REPLICAS['waiting_lariska']))
                await message.answer(get_ai_answer(message.text))

            else:
                await message.reply(choice(REPLICAS['n_users']))
        else:
            await message.reply(choice(REPLICAS['n_users']))


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_reply(message: types.Message):
    await message.reply(choice(REPLICAS['photo_reply']))

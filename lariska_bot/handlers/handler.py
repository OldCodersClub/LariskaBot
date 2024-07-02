import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram import F
from aiogram.types import Message

import pytz
from datetime import datetime, timedelta
from random import choice

from lariska_bot.config_data import (MESSAGES, REPLICAS, USERS, WORKS_CHATS,
                                     BOT_FIRST_NAME, RATING_LIMIT, FLOOD_RATE, L_USERS)
from lariska_bot.handlers.controllers import (flood_controlling, get_answer, get_ai_answer)
from create_dp import dp

logger = logging.getLogger(__name__)
router = Router()

@dp.message(F.Text.contains('говно'))
async def skirmish_reply(message: Message):
    await message.reply(MESSAGES['skirmish'])


@dp.message(F.Text.contains('привет'))
async def hello_reply(message: Message):
    await message.reply(MESSAGES['hello'])


@dp.message(F.Text.contains('с чего начать'))
async def where_to_begin(message: Message):
    await message.reply(MESSAGES['start_here'])
    await message.answer(MESSAGES['start_video'])
    await message.answer(MESSAGES['message_links'])


@dp.message(F.Text.contains('https://t.me/oldcoders_bar'))
async def bar_reply(message: Message):
    await message.reply(choice(REPLICAS['bar']))


@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer(MESSAGES['welcome'])


@dp.message(F.text)
# @dp.throttled(flood_controlling, rate=FLOOD_RATE)
async def text_reply(message: Message):
    logger.debug(f'Message: {message.text}')
    username = message.from_user.username
    userid = message.from_user.id

    # Если имя пользователя Телеграмм пустое создаем имя пользователя из userid
    if username is None:
        username = 'User_' + str(userid)

    user_day = USERS.get(username)
    logging.debug(f'User id:  {userid}')
    logging.debug(f'User name:  {username}')
    logging.debug(f'User day:  {user_day}')

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


@dp.message(F.photo)
async def photo_reply(message: Message):
    await message.reply(choice(REPLICAS['photo_reply']))

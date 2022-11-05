import random
from datetime import datetime, timedelta

import pytz
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile

from lariska_bot.dispatcher import dp
from lariska_bot.handlers.messages import *
from lariska_bot.handlers.throttling import flood_controlling
from lariska_bot.handlers.users import users
from lariska_bot.utils import get_list_from_file, get_word_list


DIRTY_WORDS = list(get_list_from_file('lariska_bot/res/dirty_words.txt'))


# @dp.message_handler(lambda msg:
#                     any(word in get_word_list(msg) for word in DIRTY_WORDS))
# async def dont_swear(message: types.Message):
#     await message.reply_photo(
#         photo=InputFile('lariska_bot/res/dont_swear.jpg'),
#         caption=get_dont_swear()
#     )


@dp.message_handler(Text(contains=['говно'], ignore_case=True))
async def skirmish_reply(message: types.Message):
    await message.reply(dont_skirmish())


@dp.message_handler(Text(contains=['лариска', 'дура'], ignore_case=True))
async def call_names_reply(message: types.Message):
    await message.reply(dont_call_names())


@dp.message_handler(Text(contains=['лариска', 'фас'], ignore_case=True))
async def attack_reply(message: types.Message):
    await message.reply(get_attack_reply())


@dp.message_handler(Text(contains=['привет'], ignore_case=True))
async def hello_reply(message: types.Message):
    await message.reply(get_hello())


@dp.message_handler(Text(contains=['с чего начать'], ignore_case=True))
async def where_to_begin(message: types.Message):
    await message.reply(get_start_here())
    await message.answer(get_start_video())
    await message.answer('Там много полезных ссылок под видео.')


@dp.message_handler(Text(contains=['наш репозиторий'], ignore_case=True))
async def our_repository_reply(message: types.Message):
    await message.reply(get_repo())


@dp.message_handler(Text(contains=['наша репа'], ignore_case=True))
async def our_repo_reply(message: types.Message):
    await message.reply(get_repo())


@dp.message_handler(Text(contains=['лариска', 'бот'], ignore_case=True))
async def lariska_bot_reply(message: types.Message):
    await message.reply(get_lariska_bot())
    await message.answer(get_forks())


@dp.message_handler(commands=get_repo_list())
async def repo_answer(message: types.Message):
    await message.answer(get_repo())


@dp.message_handler(commands=get_video_list())
async def youtube_answer(message: types.Message):
    await message.answer(get_youtube())


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(get_welcome(), parse_mode=types.ParseMode.MARKDOWN)


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
        await message.reply(random.choice(user_dict['greetings']))


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_reply(message: types.Message):
    await message.reply('Красивенько 😍')

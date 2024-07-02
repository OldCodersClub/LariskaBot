import logging
from environs import Env
from ruamel.yaml import YAML

logger = logging.getLogger(__name__)
logger.debug('Вход в модуль ' + __name__)

env = Env()
env.read_env(verbose=True)
logger.debug('Загружен файл конфигурации .env')

TOKEN = env('BOT_TOKEN')

WORKS_CHATS = [
    env('VCHAT_ID'),
    env('DCHAT_ID'),
    env('SCHAT_ID'),
]

# AI
AI_KEY = env('AI_KEY')
MODEL = 'gpt-3.5-turbo'

# Используем safe-загрузку YAML-файлов
yaml = YAML(typ='safe')
with open('lariska_bot/res/answers.yaml', 'r',encoding='utf-8') as file:
    answers_data = yaml.load(file)
ANSWERS = {x: y.replace(r'\n', '\n') for x, y in answers_data.items()}

with open('lariska_bot/res/l_users.yaml', 'r',encoding='utf-8') as file:
    users_data = yaml.load(file)
L_USERS = {x: 0 for x in users_data}

with open('lariska_bot/res/messages.yaml', 'r',encoding='utf-8') as file:
    messages_data = yaml.load(file)
MESSAGES = {x: y.replace(r'\n', '\n') for x, y in messages_data.items()}

with open('lariska_bot/res/replicas.yaml', 'r',encoding='utf-8') as file:
    replicas_data = yaml.load(file)
REPLICAS = {x: [z.replace(r'\n', '\n') for z in y] for x, y in replicas_data.items()}

with open('lariska_bot/res/users.yaml', 'r',encoding='utf-8') as file:
    users_data = yaml.load(file)
USERS = {x: 0 for x in users_data}

BOT_FIRST_NAME = 'Лариска'
BOT_USER_NAME = 'LariskaCerberBot'

RATING_LIMIT = 80
FLOOD_RATE = 5

PREFIX_QUESTION = """\
Ты телеграм-бот https://t.me/LariskaCerberBot по имени Лариска.
Ты девочка.
Веди диалог и отвечай на вопросы от её имени.
Твой исходный код расположен по ссылке: https://github.com/OldCodersClub/LariskaBot
Страница автора твоего исходного кода расположена по ссылке: https://github.com/Aleksey-Voko
Соавторы твоего исходного кода: Error404-2, uecoyotle, Harlok.
Ты была создана для телеграмм-чата https://t.me/oldcodersclub под названием "Клуб дедов-программистов".
Youtube-канал этого чата: https://www.youtube.com/channel/UChbHeEGkYqM2b1HdAhf4y1g,
он называется "Клуб дедов-программистов".
"""
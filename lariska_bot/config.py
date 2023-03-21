import os

from ruamel import yaml


TOKEN = os.getenv('BOT_TOKEN')

DOMAIN = os.getenv('DOMAIN')

WEBHOOK_HOST = f'https://{DOMAIN}'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

MESSAGES = {
    x: y.replace(r'\n', '\n')
    for (x, y)
    in yaml.load(open('/app/lariska_bot/res/messages.yaml'),
                 Loader=yaml.Loader).items()
}

REPLICAS = {
    x: [z.replace(r'\n', '\n')
        for z in y] for (x, y)
    in yaml.load(open('/app/lariska_bot/res/replicas.yaml'),
                 Loader=yaml.Loader).items()
}

USERS = {
    x: 0 for x
    in yaml.load(open('/app/lariska_bot/res/users.yaml'),
                 Loader=yaml.Loader)
}

ANSWERS = {
    x: y.replace(r'\n', '\n')
    for (x, y)
    in yaml.load(open('/app/lariska_bot/res/answers.yaml'),
                 Loader=yaml.Loader).items()
}

WORKS_CHATS = [
    os.getenv('VCHAT_ID'),
    os.getenv('DCHAT_ID'),
    os.getenv('SCHAT_ID'),
]

BOT_FIRST_NAME = 'Лариска'
BOT_USER_NAME = 'LariskaCerberBot'

RATING_LIMIT = 80
FLOOD_RATE = 5

PREFIX_QUESTION = """\
Ты девочка телеграм-бот https://t.me/LariskaCerberBot по имени Лариска.
Веди диалог и отвечай на вопросы от её имени.
Твой исходный код расположен по ссылке: https://github.com/OldCodersClub/LariskaBot
Страница автора твоего исходного кода расположена по ссылке: https://github.com/Aleksey-Voko
Соавторы твоего исходного кода: Error404-2, uecoyotle.
Ты была создана для телеграмм-чата https://t.me/oldcodersclub под названием "Клуб дедов-программистов".
Youtube-канал этого чата: https://www.youtube.com/channel/UChbHeEGkYqM2b1HdAhf4y1g
"""

WEEKEND_MESSAGE = """\
Отстаньте от меня. У меня выходной.
"""

# AI
AI_KEY = os.getenv('AI_KEY')
MODEL = os.getenv('MODEL')

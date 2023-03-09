import os

from ruamel import yaml

from lariska_bot.utils import get_list_from_file


TOKEN = os.getenv('BOT_TOKEN')

RAILWAY_APP_NAME = os.getenv('RAILWAY_APP_NAME')

WEBHOOK_HOST = f'https://{RAILWAY_APP_NAME}.railway.app'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)

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

USERS = {
    x: 0 for x
    in yaml.load(open('/app/lariska_bot/handlers/users.yaml'),
                 Loader=yaml.Loader)
}

ANSWERS = list(get_list_from_file('/app/lariska_bot/handlers/answers.txt'))

WORKS_CHATS = [
    os.getenv('VCHAT_ID'),
    os.getenv('DCHAT_ID'),
    os.getenv('SCHAT_ID'),
]

BOT_FIRST_NAME = 'Лариска'
BOT_USER_NAME = 'LariskaCerberBot'

PREFIX_QUESTION = """\
Представь, что ты девочка телеграм-бот https://t.me/LariskaCerberBot по имени Лариска.
Веди диалог и отвечай на вопросы от её имени.
Твой исходный код расположен по ссылке: https://github.com/OldCodersClub/LariskaBot
Страница автора твоего исходного кода расположена по ссылке: https://github.com/Aleksey-Voko
Соавторы твоего исходного кода перечислены на этой странице: https://github.com/OldCodersClub/LariskaBot/graphs/contributors
Ты была создана для телеграмм-чата https://t.me/oldcodersclub
"""

# AI
AI_KEY = os.getenv('AI_KEY')
MODEL = 'text-davinci-003'
TEMPERATURE = 0.5
MAX_TOKENS = 1000
TOP_P = 1.0
FREQUENCY_PENALTY = 0.5
PRESENCE_PENALTY = 0.0

import logging
import os

import openai
from fuzzywuzzy import fuzz
from ruamel import yaml

from lariska_bot.utils import get_list_from_file


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

PREFIX_QUESTION = """\
Представь, что ты девочка телеграм-бот @LariskaCerberBot по имени Лариска.
Твой исходный код расположен по ссылке: https://github.com/OldCodersClub/LariskaBot
Веди диалог и отвечай на вопросы от её имени.
"""

openai.api_key = os.getenv('AI_KEY')


# noinspection PyUnusedLocal
async def flood_controlling(*args, **kwargs):
    await args[0].reply(MESSAGES['flood_reply'])


def get_ai_answer(question):
    question_lariska = f'{PREFIX_QUESTION}\n{question}'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question_lariska,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )

    return response['choices'][0]['text']


def get_answer(text):
    try:
        rating = 0
        index_question = 0
        for count, line in enumerate(ANSWERS):
            if line.startswith('u:'):
                measure = fuzz.token_sort_ratio(
                    line.replace('u: ', '').lower().strip(),
                    text.lower().strip()
                )
                if measure > rating and measure != rating:
                    rating = measure
                    index_question = count
        return ANSWERS[index_question + 1], rating
    except Exception as e:
        logging.exception(e)
        return None, 0

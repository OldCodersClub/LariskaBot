import json
import logging

import openai
import requests
from fuzzywuzzy import fuzz

from lariska_bot.config_data import (AI_KEY, MESSAGES, PREFIX_QUESTION, ANSWERS, MODEL)

logger = logging.getLogger(__name__)
openai.api_key = AI_KEY

def get_answer(text:str):
    text = text.lower().strip()
    logger.debug(f"text: {text}")
    try:
        rating = 0
        answer = None
        for key, val in ANSWERS.items():
             # Этот код пытается найти наиболее подходящий ответ для заданного входного текста.
            # Это простой пример того, как программа может сравнивать различные входные данные
            # и находить наилучшее соответствие.
            measure = fuzz.token_sort_ratio(key.lower().strip(), text)

            if measure > rating and measure != rating:
                logger.debug(f"key:  {key}, val: {val}, measure: {measure}")
                rating = measure
                answer = val
        return answer, rating
    except Exception as e:
        logging.exception(e)
        return None, 0

async def flood_controlling(*args, **kwargs):
    await args[0].reply(MESSAGES['flood_reply'])
def get_ai_answer(question):
    question_lariska = f'{PREFIX_QUESTION}\n{question}'
    response = openai.ChatCompletion.create(
        model=MODEL,messages=[{"role": "user", "content": question_lariska},]
    )
    return response['choices'][0]['message']['content']


def is_work_day(year: int, month: int, day: int) -> str:
    url = f'https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant{year}.json'
    response = requests.get(url)
    days = json.loads(response.text)
    return f'{year:04}-{month:02}-{day:02}' not in days['holidays']

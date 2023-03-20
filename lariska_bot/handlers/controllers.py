import json
import logging

import openai
import requests
from fuzzywuzzy import fuzz

from lariska_bot.config import (AI_KEY, MESSAGES, PREFIX_QUESTION, ANSWERS,
                                MODEL, TEMPERATURE, MAX_TOKENS, TOP_P,
                                FREQUENCY_PENALTY, PRESENCE_PENALTY)


openai.api_key = AI_KEY


# noinspection PyUnusedLocal
async def flood_controlling(*args, **kwargs):
    await args[0].reply(MESSAGES['flood_reply'])


def get_ai_answer(question):
    question_lariska = f'{PREFIX_QUESTION}\n{question}'

    # response = openai.Completion.create(
    #     model=MODEL,
    #     prompt=question_lariska,
    #     temperature=TEMPERATURE,
    #     max_tokens=MAX_TOKENS,
    #     top_p=TOP_P,
    #     frequency_penalty=FREQUENCY_PENALTY,
    #     presence_penalty=PRESENCE_PENALTY,
    # )
    #
    # return response['choices'][0]['text']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question_lariska},
        ]
    )

    return response['choices'][0]['message']['content']


def get_answer(text):
    text = text.lower().strip()
    try:
        rating = 0
        answer = None
        for key, val in ANSWERS.items():
            measure = fuzz.token_sort_ratio(key.lower().strip(), text)
            if measure > rating and measure != rating:
                rating = measure
                answer = val
        return answer, rating
    except Exception as e:
        logging.exception(e)
        return None, 0


def is_work_day(year, month, day):
    url = f'https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant{year}.json'
    response = requests.get(url)
    days = json.loads(response.text)
    return f'{year:04}-{month:02}-{day:02}' not in days['holidays']

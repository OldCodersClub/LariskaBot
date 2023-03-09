import logging
import os

import openai
from fuzzywuzzy import fuzz

from lariska_bot.config import (MESSAGES, PREFIX_QUESTION, LING_MODEL,
                                TEMPERATURE, MAX_TOKENS, TOP_P,
                                FREQUENCY_PENALTY, PRESENCE_PENALTY, ANSWERS,
                                AI_KEY)


openai.api_key = os.getenv(AI_KEY)


# noinspection PyUnusedLocal
async def flood_controlling(*args, **kwargs):
    await args[0].reply(MESSAGES['flood_reply'])


def get_ai_answer(question):
    question_lariska = f'{PREFIX_QUESTION}\n{question}'

    response = openai.Completion.create(
        model=LING_MODEL,
        prompt=question_lariska,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
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

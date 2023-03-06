import logging

from fuzzywuzzy import fuzz

from lariska_bot.utils import get_list_from_file


ANSWERS = list(get_list_from_file('/app/lariska_bot/handlers/answers.txt'))


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

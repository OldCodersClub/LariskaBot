import re
from pathlib import Path


def get_list_from_file(file_name, encoding='utf-8'):
    with open(Path(file_name), encoding=encoding) as in_file:
        for line in in_file:
            yield line.strip()


def get_word_list(sentence):
    return list(filter(
        lambda x: len(x) > 0,
        re.split(r'\W+', sentence.lower())
    ))

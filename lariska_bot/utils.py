from pathlib import Path


def get_list_from_file(file_name, encoding='utf-8'):
    with open(Path(file_name), encoding=encoding) as in_file:
        for line in in_file:
            yield line.strip()

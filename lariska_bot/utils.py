from pathlib import Path


def get_list_from_file(file_name, encoding='utf-8'):
    with open(Path(file_name), encoding=encoding) as f:
        for line in f:
            yield line.strip().replace(r'\n', '\n')

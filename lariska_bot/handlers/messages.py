from random import choice


def dont_skirmish():
    return 'Милорды, не начинайте срач пожалуйста!'


def get_hello():
    return 'Привет, дорогуша!'


def get_start_here():
    return 'Начни отсюда:\nhttps://github.com/OldCodersClub/faq'


def get_start_video():
    return 'Или отсюда:\nhttps://www.youtube.com/watch?v=_PfQvdDq_bY'


def get_message_links():
    return 'Там много полезных ссылок под видео.'


def get_lariska_bot():
    return (
        'Да. Я бот.'
        '\nВот репозиторий:'
        '\nhttps://github.com/OldCodersClub/LariskaBot'
    )


def get_forks():
    return 'Можете форкать, реквестить и деплоить'


def get_photo_reply():
    return 'Красивенько 😍'


def get_flood_reply():
    return (
        'Помедленнее, дорогуша!'
        '\nЯ записываю...'
    )


def get_welcome():
    return ('Привет!'
            '\nЯ Лариска - бот из Клуба дедов-программистов.'
            '\nВсе мои команды секретные.'
            '\nИх можно только в репе посмотреть:'
            '\nhttps://github.com/OldCodersClub')


bar_reply = [
    'Я тоже хочу в бар!',
    'А можно и мне тоже в бар?',
    'Все идём в бар!',
]


def get_bar_reply():
    return choice(bar_reply)

# LariskaBot - telegram-bot (Python, [aiogram](https://aiogram.dev/))

[![stars](https://img.shields.io/github/stars/OldCodersClub/LariskaBot?logoColor=red&style=social)](https://github.com/OldCodersClub/LariskaBot/stargazers)
[![forks](https://img.shields.io/github/forks/OldCodersClub/LariskaBot?logoColor=red&style=social)](https://github.com/OldCodersClub/LariskaBot/forks)
[![watchers](https://img.shields.io/github/watchers/OldCodersClub/LariskaBot?logoColor=red&style=social)](https://github.com/OldCodersClub/LariskaBot/watchers)
[![wakatime](https://wakatime.com/badge/user/8cc8aa38-4041-409b-9d27-a85e5b897ad4/project/9429f9d1-0e7c-4945-a1fd-9e085f3d6067.svg?style=social)](https://wakatime.com/@Voko/projects/xqfpkutwnj?start=2023-03-06&end=2023-03-12)

Телеграмм-бот для чата [@OldCodersClub](https://t.me/oldcodersclub)

[![Lariska](lariska_bot/res/avatar.jpg)](https://t.me/oldcodersclub)

Бот использует приоритеты при поиске и генерации ответов для пользователей:

- фильтры (handler) aiogram (самый приоритетный)
- готовые ответы для конкретных пользователей (приветствие при первом сообщении пользователя, один раз за сутки)
- собственная база готовых ответов с использованием [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/) (расстояние Левенштейна) для нечёткого сопоставления вопросов и ответов (настроен на 80% совпадение)
- [OpenAI API](https://platform.openai.com/docs/api-reference/) (срабатывает только если обратиться к боту по имени)

Любой ниже расположенный фильтр срабатывает, только если были пропущены все расположенные выше.

### Запуск в Докере

Создать и запустить контейнер:

```bash
$ export BOT_TOKEN=<BOT_TOKEN>
$ export AI_KEY=<AI_KEY>
$ export VCHAT_ID=<VCHAT_ID>
$ export DCHAT_ID=<DCHAT_ID>
$ export SCHAT_ID=<SCHAT_ID>
$ docker-compose up -d
```

Остановить запущенный контейнер:

```bash
$ docker-compose stop
```

Запустить остановленный контейнер:

```bash
$ docker-compose start
```

Остановить и удалить контейнер и сеть:

```bash
$ docker-compose down
```

Удалить докер-образ:

```bash
$ docker rmi lariska_bot
```

Очистить логи:

```bash
$ sudo rm -rf logs/*
```

### [Пустой шаблон для деплоя](https://railway.app/template/-S3lVz?referralCode=jUyx2Z)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/-S3lVz?referralCode=jUyx2Z)

#### Переменные

- `BOT_TOKEN` - токен Telegram-бота
- `CHAT_ID` - ID чата, в котором разрешено работать боту.
- `AI_KEY` - OpenAI API токен
- `DOMAIN` - URL-адрес с названием приложения. После развертывания перейдите в настройки проекта (`Settings`) и скопируйте домен из раздела `Domains`. Это должно быть похоже на `worker-production-XXXX.up.railway.app`. Это и будет значение для переменной `DOMAIN`.

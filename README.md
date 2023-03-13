# LariskaBot - telegram-bot (Python, [aiogram](https://aiogram.dev/))

[![wakatime](https://wakatime.com/badge/user/8cc8aa38-4041-409b-9d27-a85e5b897ad4/project/9429f9d1-0e7c-4945-a1fd-9e085f3d6067.svg)](https://wakatime.com/@Voko/projects/xqfpkutwnj?start=2023-03-06&end=2023-03-12)

Телеграмм-бот для чата [@OldCodersClub](https://t.me/oldcodersclub)

Бот использует приоритеты при поиске и генерации ответов для пользователей:

- фильтры (handler) aiogram (самый приоритетный)
- готовые ответы для конкретных пользователей (приветствие при первом сообщении пользователя, один раз за сутки)
- собственная база готовых ответов с использованием [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/) (расстояние Левенштейна) для нечёткого сопоставления вопросов и ответов (настроен на 80% совпадение)
- [OpenAI API](https://platform.openai.com/docs/api-reference/) (срабатывает только если обратиться к боту по имени)

Любой ниже расположенный фильтр срабатывает, только если были пропущены все расположенные выше.

### [Пустой шаблон для деплоя](https://railway.app/template/U-zkJQ?referralCode=jUyx2Z)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/U-zkJQ?referralCode=jUyx2Z)

#### Переменные

`BOT_TOKEN` - токен телеграмм бота.  
`RAILWAY_APP_NAME` - часть урл приложения (можно получить при деплое).  
`CHAT_ID` - ID телеграмм чата, в котором разрешено работать боту. Необходимо добавить в список `WORKS_CHATS` в файле [`config.py`](lariska_bot/config.py). Можно добавить несколько.  
`AI_KEY` - токен OpenAI API.

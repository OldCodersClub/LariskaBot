from dataclasses import dataclass
from lariska_bot.config_data import TOKEN


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту

@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и возвращать
# экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str | None = None) -> Config:
   return Config(
        tg_bot = TgBot(token=TOKEN)
    )
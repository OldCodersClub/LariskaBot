from lariska_bot.handlers.messages import get_flood_reply


# noinspection PyUnusedLocal
async def flood_controlling(*args, **kwargs):
    await args[0].reply(get_flood_reply())

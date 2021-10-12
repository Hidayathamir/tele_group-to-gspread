import json

from telethon import TelegramClient, events


async def write_group_id(event: events.NewMessage) -> None:
    if event.is_group:
        chat_id = event.chat_id
        name = event.chat.title
        with open("src/group_id.json") as jfile:
            data = json.load(jfile)
        data[name] = chat_id
        with open("src/group_id.json", "w+") as jfile:
            json.dump(data, jfile, indent=4)
        print("update src/group_id.json")


def get_group_id(
    SESSION: str, API_ID: int, API_HASH: str, BOT_TOKEN: str
) -> None:
    bot = TelegramClient(SESSION, API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    bot.add_event_handler(
        write_group_id,
        events.NewMessage(incoming=True),
    )
    bot.run_until_disconnected()

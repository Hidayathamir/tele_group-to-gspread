from telethon import TelegramClient, events


async def echo(event: events.NewMessage) -> None:
    # TODO: read message then add to gspread
    """
    now it can read message like this
        /report
        nama : hidayat
        umur : 17
    then got like this
        {
            "nama" : "hidayat",
            "umur" : "17",
        }
    """
    text = event.text.split("\n")
    if text[0] == "/report":
        await event.respond(event.text)
        data = {}
        for col in text[1:]:
            index = col.index(":")
            key = col[:index].strip()
            value = col[index + 1 :].strip()
            data[key] = value
        print(data)


def main(
    SESSION: str, API_ID: int, API_HASH: str, BOT_TOKEN: str, chat_id: int
) -> None:
    bot = TelegramClient(SESSION, API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    bot.add_event_handler(
        echo,
        events.NewMessage(
            incoming=True,
            chats=chat_id,
        ),
    )
    bot.run_until_disconnected()

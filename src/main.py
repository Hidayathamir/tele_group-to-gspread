from telethon import TelegramClient, events


async def echo(event: events.NewMessage) -> None:
    await event.respond(event.text)


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

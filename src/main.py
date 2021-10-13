from telethon import TelegramClient, events

from .my_module import extract_data, extract_text_report, reply_success


def main(
    SESSION: str, API_ID: int, API_HASH: str, BOT_TOKEN: str, chat_id: int
) -> None:
    bot = TelegramClient(SESSION, API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    bot.add_event_handler(
        get_report,
        events.NewMessage(incoming=True, chats=chat_id),
    )
    bot.run_until_disconnected()


async def get_report(event: events.NewMessage) -> None:
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
    text, text_is_report, report_has_data = extract_text_report(event)
    if text_is_report:
        if report_has_data:
            try:
                data = extract_data(text)
                await reply_success(event, data)
            except ValueError as e:
                await event.message.reply(str(e))
                return None
            print(data)
        else:
            await event.message.reply("Mohon masukkan data.")

import gspread
from gspread.client import Client
from gspread.models import Worksheet
from oauth2client.service_account import ServiceAccountCredentials
from telethon import TelegramClient, events

from .google_spread import update_google_spread
from .my_module import extract_data, extract_text_report, reply_success

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
creds: ServiceAccountCredentials = (
    ServiceAccountCredentials.from_json_keyfile_name("keys.json")
)
client: Client = gspread.authorize(creds)
sheet: Worksheet = client.open("test_api").sheet1


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
            except ValueError as e:
                await event.message.reply(str(e))
                return None
            try:
                update_google_spread(sheet, data)
            except ValueError as e:
                await event.message.reply(str(e))
                return None
            await reply_success(event, data)
        else:
            await event.message.reply("Mohon masukkan data.")

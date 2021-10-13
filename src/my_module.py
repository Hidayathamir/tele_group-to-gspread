from typing import Dict, List, Tuple

from telethon import TelegramClient, events


def extract_text_report(
    event: events.NewMessage,
) -> Tuple[List[str], bool, bool]:
    text = event.text.split("\n")
    text_is_report = text[0] == "/report"
    report_has_data = len(text) > 1
    return (text, text_is_report, report_has_data)


def extract_data(text: List[str]) -> Dict[str, str]:
    data = {}
    for col in text[1:]:
        try:
            index = col.index(":")
        except ValueError:
            raise ValueError("Mohon gunakan format pelaporan.")
        key = col[:index].strip()
        value = col[index + 1 :].strip()
        data[key] = value
    return data


async def reply_success(event: TelegramClient, data: Dict[str, str]) -> None:
    text_reply = "Data diterima."
    for k, v in data.items():
        text_reply += f"\n{k} = {v}"
    await event.message.reply(text_reply)

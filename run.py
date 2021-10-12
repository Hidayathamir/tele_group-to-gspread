import json
from sys import argv

from decouple import config

from src.get_group_id import get_group_id
from src.main import main


def run() -> None:
    try:
        # run with args
        arg = argv[1]
    except IndexError:
        # run without args
        raise ValueError(
            f"Need to pass argument, either group name or get-group-id"
        )

    API_ID = config("API_ID", cast=int)
    API_HASH = config("API_HASH")
    SESSION = config("SESSION")
    BOT_TOKEN = config("BOT_TOKEN")

    if arg == "get-group-id":
        print("Run get_group_id")
        print("Silahkan chat di grup")
        get_group_id(SESSION, API_ID, API_HASH, BOT_TOKEN)
    else:
        with open("src/group_id.json") as jfile:
            data = json.load(jfile)
        try:
            chat_id = int(data[arg])
        except KeyError:
            raise ValueError(f"src/group_id.json does not have {arg}")
        print("Bot is running")
        main(SESSION, API_ID, API_HASH, BOT_TOKEN, chat_id)


if __name__ == "__main__":
    run()

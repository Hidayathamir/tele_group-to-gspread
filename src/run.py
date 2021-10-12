from main import main
from decouple import config


def run() -> None:
    API_ID = config("API_ID", cast=int)
    API_HASH = config("API_HASH")
    SESSION = config("SESSION")
    BOT_TOKEN = config("BOT_TOKEN")
    CHATS = config("CHATS")
    print("Run Main")
    main(SESSION, API_ID, API_HASH, BOT_TOKEN, CHATS)


if __name__ == "__main__":
    run()

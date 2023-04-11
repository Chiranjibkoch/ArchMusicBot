from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/9b90a015b665192a2f5e7.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph//file/a74ac70eb1a97b8195be9.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+_6KcBmU8uWFjNmU1")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/secret_chatting_world")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://telegra.ph//file/81e48b20c8d5ab410c5b4.jpg"

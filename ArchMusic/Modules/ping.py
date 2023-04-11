import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from ArchMusic import BOT_NAME, StartTime, app
from ArchMusic.Helpers import get_readable_time


@app.on_message(filters.command("ping"))
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} PONG......"
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    async def edit_message():
        await hmm.edit_text(
            f""" <b><u>{BOT_NAME} SYSTEM STATS:</u></b>
working with a good ping `{resp}MS` uptime {uptime} ram {mem} cpu loaded {cpu} disk {disk}
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("SUPPORT", url=config.SUPPORT_CHAT),
                    ],
                ]
            ),
        )

    await edit_message()
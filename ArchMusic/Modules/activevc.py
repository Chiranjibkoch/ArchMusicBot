from pyrogram import filters
from pyrogram.types import Message

from ArchMusic import SUDOERS, app
from ArchMusic.Helpers.active import get_active_chats
from ArchMusic.Helpers.inline import close_key


@app.on_message(filters.command("activevc") & SUDOERS)
async def activevc(_, message):
    mystic = await message.reply_text("» Getting active voicechats list...")
    chats = await get_active_chats()
    text = ""
    j = 0
    for chat in chats:
        try:
            title = (await app.get_chat(chat)).title
        except Exception:
            title = "Private chat"
        if (await app.get_chat(chat)).username:
            user = (await app.get_chat(chat)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{chat}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("No active voicechats on musicbot...")
    else:
        await mystic.edit_text(
            f"**List of currently active voicechats on musicbot :**\n\n{text}",
            reply_markup=close_key,
            disable_web_page_preview=True,
        )

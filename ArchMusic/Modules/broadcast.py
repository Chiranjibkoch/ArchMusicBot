import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from ArchMusic import app


@app.on_message(filters.command("broadcast") & filters.user("me"))
async def broadcast(_, message: Message):
    brep = await message.reply_text("Assistant Broadcast Started...")
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.reply_to_message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Example:**\n\n/broadcast [message] or [reply to a message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    async for dialog in app.iter_dialogs():
        chats.append(int(dialog.chat.id))
    for i in chats:
        try:
            await app.forward_messages(
                i, y, x
            ) if message.reply_to_message else await app.send_message(i, text=query)
            sent += 1
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await brep.edit_text(f"**Broadcasted message in {sent} chats.**")
    except:
        await message.reply_text(f"**Broadcasted message in {sent} chats.**")

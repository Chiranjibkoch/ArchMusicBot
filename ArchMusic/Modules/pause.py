from pyrogram import filters
from pyrogram.types import Message

from ArchMusic import app, pytgcalls
from ArchMusic.Helpers import admin_check, close_key, is_streaming, stream_off


@app.on_message(filters.command(["pause"]) & filters.group)
@admin_check
async def pause_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if not await is_streaming(message.chat.id):
        return await message.reply_text(
            "Did You Remember That You resume stream?"
        )

    await pytgcalls.pause_stream(message.chat.id)
    await stream_off(message.chat.id)
    return await message.reply_text(
        text=f"Pause \n│ \nBy : {message.from_user.mention} ",
        reply_markup=close_key,
    )

from pyrogram import filters
from pyrogram.types import Message

from ArchMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("Changing Assistant Profile Pic.")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"{ASS_MENTION} Your Profile Pic Successfully Set In Assistant Account"
            )
        except:
            return await fuk.edit_text("Failed To Change Profile Piᴄ.")
    else:
        await message.reply_text(
            "Reply To A Photo For Change Assistant Profile Pic."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "Deletion Successfully"
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("Failed To Delete Assistant Profile pic")


@app.on_message(filters.command(["assbio", "setbio"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"{ASS_MENTION} Bio Has Been Successfully Changed"
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"{ASS_MENTION} Bio Changed")
    else:
        return await message.reply_text(
            "Drop Text For Change Assistant Bio"
        )


@app.on_message(filters.command(["assname", "setname"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"{ASS_MENTION} Your Assistant Name Changed"
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"{ASS_MENTION} name Changed successfully .")
    else:
        return await message.reply_text(
            "Drop Or Reply To assistant New Name"
        )

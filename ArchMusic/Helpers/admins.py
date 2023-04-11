from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, Message

from ArchMusic import SUDOERS, app

from .active import is_active_chat


def admin_check(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if not await is_active_chat(message.chat.id):
            return await message.reply_text("Bot isn't streaming on videochat.")

        if message.from_user.id in SUDOERS:
            return await func(_, message)

        check = await app.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "I'm sorry, but it seems like you do not have admin privileges. Could you please stay within your limits? Thank you."
            )

        admin = (
            await app.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, message)
        else:
            return await message.reply_text(
                "Could you please refrain from managing video chats as you do not have the necessary permissions? Thank you for staying within your limits."
            )

    return non_admin


def admin_check_cb(func: Callable) -> Callable:
    async def cb_non_admin(_, query: CallbackQuery):
        if not await is_active_chat(query.message.chat.id):
            return await query.answer(
                "Bot isn't streaming on videochat.", show_alert=True
            )

        if query.from_user.id in SUDOERS:
            return await func(_, query)

        try:
            check = await app.get_chat_member(query.message.chat.id, query.from_user.id)
        except:
            return
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await query.answer(
                "I'm sorry, but it seems like you do not have admin privileges. Could you please stay within your limits? Thank you.",
                show_alert=True,
            )

        admin = (
            await app.get_chat_member(query.message.chat.id, query.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, query)
        else:
            return await query.answer(
                "I apologize for any inconvenience, but it appears that you do not have the necessary permissions to manage videochats. Could you please kindly stay within your limits? Thank you.",
                show_alert=True,
            )

    return cb_non_admin

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ArchMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="Close", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▶️", callback_data="resume_cb"),
            InlineKeyboardButton(text="⏸︎", callback_data="pause_cb"),
            InlineKeyboardButton(text="⏯️", callback_data="skip_cb"),
            InlineKeyboardButton(text="⏹︎", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="ADD ME YOUR GROUP",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="HELP & COMMANDS", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="SUPPORT CHANNEL", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="SUPPORT CHAT", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(text="DEVELOPER", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="ADD ME YOUR GROUP",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="SUPPORT CHANNEL", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="SUPPORT CHAT", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(text="DEVELOPER", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="EVERYONE",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="SUDO", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="OWNER", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="BACK", callback_data="fallen_home"),
        InlineKeyboardButton(text="CLOSE", callback_data="close"),
    ],
]

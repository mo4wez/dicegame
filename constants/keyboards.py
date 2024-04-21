from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from .messages import (
    PLAY_GAME_TEXT,
    TRANSFORM_COINS_TEXT,
    USER_ACCOUNT_TEXT,
    SUPPORT_TEXT,
    INCREASE_INVENTORY_TEXT,
    BOOK_ICON_TEXT,
    CANCEL_TEXT,
    INVITE_USER_TEXT,
    TRANSFORM_NITROSEEN_TEXT,
    BACK_TEXT,
    )

JOIN_TO_CHANNEL_KEYBOARD = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton('dice game channel', url='https://t.me/dicegametestpy')]
    ]
)

MAIN_MENU_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=PLAY_GAME_TEXT)],
        [KeyboardButton(text=TRANSFORM_COINS_TEXT), KeyboardButton(text=USER_ACCOUNT_TEXT)],
        [KeyboardButton(text=SUPPORT_TEXT), KeyboardButton(INCREASE_INVENTORY_TEXT)],
        [KeyboardButton(text=BOOK_ICON_TEXT)]
    ],
    resize_keyboard=True
)

INCREASE_INVENTORY_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=INVITE_USER_TEXT), KeyboardButton(text=TRANSFORM_NITROSEEN_TEXT)],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)

CANCEL_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=CANCEL_TEXT)]
    ],
    resize_keyboard=True
)
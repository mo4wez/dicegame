from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from .messages import (
    PLAY_GAME_TEXT,
    TRANSFORM_COINS_TEXT,
    USER_ACCOUNT_TEXT,
    SUPPORT_TEXT,
    INCREASE_INVENTORY_TEXT,
    INFORMATION_TEXT
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
        [KeyboardButton(text=INFORMATION_TEXT)]
    ],
    resize_keyboard=True
)
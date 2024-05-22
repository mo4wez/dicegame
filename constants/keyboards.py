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
    DICE_GAME_TEXT,
    BOWLING_GAME_TEXT,
    DART_GAME_TEXT,
    BASKETBALL_GAME_TEXT,
    FUTBALL_GAME_TEXT,
    SLOTMACHINE_GAME_TEXT,
    DICE_BET_ON_EVEN,
    DICE_BET_ON_ODD,
    MAIN_CHANNEL_LINK_TEXT,
    BOWLING_GAME_0,
    BOWLING_GAME_1,
    BOWLING_GAME_3,
    BOWLING_GAME_4,
    BOWLING_GAME_5,
    BOWLING_GAME_6,
    ITS_GOAL,
    ITS_NOT_GOAL,
    FUTBALL_GAME_ITS_GOAL,
    FUTBALL_GAME_ITS_NOT_GOAL,
    DART_GAME_HITS,
    DART_GAME_NOT_HITS,
    DART_GAME_RED,
    DART_GAME_WHITE,
    DO_BET,
    )

JOIN_TO_CHANNEL_KEYBOARD = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton('dice game channel', url=MAIN_CHANNEL_LINK_TEXT)]
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

GAMES_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=DICE_GAME_TEXT), KeyboardButton(text=BOWLING_GAME_TEXT)],
        [KeyboardButton(text=BASKETBALL_GAME_TEXT), KeyboardButton(text=FUTBALL_GAME_TEXT)],
        [KeyboardButton(text=DART_GAME_TEXT), KeyboardButton(text=SLOTMACHINE_GAME_TEXT)],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)
DICE_GAME_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=DICE_BET_ON_EVEN), KeyboardButton(text=DICE_BET_ON_ODD)],
        [KeyboardButton(text=number) for number in range(1,7)],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)

BOWLING_GAME_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=BOWLING_GAME_0), KeyboardButton(text=BOWLING_GAME_1)],
        [KeyboardButton(text=BOWLING_GAME_3), KeyboardButton(text=BOWLING_GAME_4)],
        [KeyboardButton(text=BOWLING_GAME_5), KeyboardButton(text=BOWLING_GAME_6)],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)

BASKETBAL_GAME_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=ITS_GOAL), KeyboardButton(text=ITS_NOT_GOAL)],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)

FUTBALL_GAME_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=FUTBALL_GAME_ITS_NOT_GOAL), KeyboardButton(text=FUTBALL_GAME_ITS_GOAL)],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)

DART_GAME_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=DART_GAME_HITS), KeyboardButton(text=DART_GAME_NOT_HITS)],
        [KeyboardButton(text=DART_GAME_RED), KeyboardButton(text=DART_GAME_WHITE)],
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)

SLOT_MACHINE_GAME_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=DO_BET)],
        [KeyboardButton(text=BACK_TEXT)]
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
BACK_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=BACK_TEXT)]
    ],
    resize_keyboard=True
)
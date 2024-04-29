from pyrogram import Client, filters
from pyromod import listen, Client
from pyrogram.types import Message

from constants.messages import (
    PLAY_GAME_TEXT,
    TRANSFORM_COINS_TEXT,
    USER_ACCOUNT_TEXT,
    SUPPORT_TEXT,
    INCREASE_INVENTORY_TEXT,
    BOOK_ICON_TEXT,
    CANCEL_TEXT,
    BOT_INSTRUCTION_MESSAGE,
    INCREASE_INVENTORY_TEXT,
    BACK_TEXT,
    RETURNED_TO_MAIN_MENU_TEXT,
)
from constants.keyboards import MAIN_MENU_KEYBOARD
from .increase_inventory_module import increase_inventory
# from .transform_coins_module import transform_coins
from .user_account_module import user_account
from .bot_support_module import bot_support
from .games_list_module import show_games_list


@Client.on_message(filters.text)
async def menu_commands(client: Client, message: Message):
    text = message.text
    chat_id = message.chat.id

    if text == PLAY_GAME_TEXT:
        await show_games_list(client, message)
    elif text == USER_ACCOUNT_TEXT:
        await user_account(client, message)
    elif text == TRANSFORM_COINS_TEXT:
        print('transform coins')
    elif text == SUPPORT_TEXT:
        await bot_support(client, message)
    elif text == INCREASE_INVENTORY_TEXT:
        await increase_inventory(client, message)
    elif text == BOOK_ICON_TEXT:
        await client.send_message(
        chat_id=chat_id,
        text=BOT_INSTRUCTION_MESSAGE,
        )
    elif text == CANCEL_TEXT:
        print('canceled')
    elif text == BACK_TEXT:
        await client.send_message(
            chat_id=chat_id,
            text=RETURNED_TO_MAIN_MENU_TEXT,
            reply_markup=MAIN_MENU_KEYBOARD
        )

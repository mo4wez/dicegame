from pyrogram import Client, filters
from pyromod import listen, Client
from pyrogram.types import Message
from models.users import User
from jdatetime import datetime

from constants.messages import (
    PLAY_GAME_TEXT,
    TRANSFORM_COINS_TEXT,
    USER_ACCOUNT_TEXT,
    SUPPORT_TEXT,
    INCREASE_INVENTORY_TEXT,
    BOOK_ICON_TEXT,
    USER_INFORMATION_TEXT,
    CANCEL_TEXT,
    BOT_INSTRUCTION_MESSAGE,
    BOT_SUPPORT_TEXT,
    INCREASE_INVENTORY_TEXT,
    BACK_TEXT,
    RETURNED_TO_MAIN_MENU_TEXT,
)
from constants.keyboards import MAIN_MENU_KEYBOARD
from .increase_inventory_module import increase_inventory
from .games import show_games_list


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

@Client.on_message(filters.regex(BOT_SUPPORT_TEXT))
async def bot_support(client: Client, message: Message):
    chat_id = message.chat.id

    await client.send_message(
        chat_id=chat_id,
        text=BOT_SUPPORT_TEXT,
    )

# transform coins
@Client.on_message(filters.regex(TRANSFORM_COINS_TEXT))
async def transform_coins(client: Client, message: Message):
    pass

# user account
@Client.on_message(filters.regex(USER_ACCOUNT_TEXT))
async def user_account(client: Client, message: Message):
    chat_id = message.chat.id
    now = datetime.now()
    formatted_datetime = now.strftime('%Y/%m/%d %H:%M:%S')

    user = User.get(User.chat_id==chat_id)
    invitations_count = str(len(user.invitations))

    await client.send_message(
        chat_id=chat_id,
        text=USER_INFORMATION_TEXT.format(user.chat_id, user.joined_at, invitations_count, user.coins, formatted_datetime),
    )
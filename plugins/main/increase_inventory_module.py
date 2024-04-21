from pyrogram import Client, filters
from pyrogram.types import Message
from models.users import User

from constants.messages import (
    INCREASE_INVENTORY_MESSAGE,
    INCREASE_INVENTORY_TEXT,
    TRANSFORM_NITROSEEN_TEXT,
    USER_INVITE_LINK,
    INVITE_MESSAGE,
    INVITE_INFO_TEXT,
    INVITE_USER_TEXT,
)
from constants.keyboards import (
    INCREASE_INVENTORY_KEYBOARD
)

import string, random, re

@Client.on_message(filters.text & filters.regex(INCREASE_INVENTORY_TEXT))
async def increase_inventory(client: Client, message: Message):
    chat_id = message.chat.id

    await client.send_message(
        chat_id=chat_id,
        text=INCREASE_INVENTORY_MESSAGE,
        reply_markup=INCREASE_INVENTORY_KEYBOARD
    )

@Client.on_message(filters.text & filters.regex(TRANSFORM_NITROSEEN_TEXT))
async def transform_nitroseen(client: Client, message: Message):
    await message.reply_text('transform')

@Client.on_message(filters.text & filters.regex(INVITE_USER_TEXT))
async def invite_user(client: Client, message: Message):
    chat_id = message.chat.id
    try:
        user = User.get(User.chat_id==chat_id)
    except User.DoesNotExist:
        await message.reply_text('کاربری وجود ندارد')
        
    await client.send_message(
        chat_id=chat_id,
        text=INVITE_MESSAGE.format(USER_INVITE_LINK.format(user.invite_link))
    )

def generate_refferal_link(length: int):
    random_str = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    cleaned_str = 'ref-' + re.sub(r'[^0-9a-zA-Z_]', '', random_str)

    return cleaned_str

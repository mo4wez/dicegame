from pyrogram import Client, filters
from pyrogram.types import Message
from models.users import User
from jdatetime import datetime
from custom_filters.join_checker_filter import is_joined_filter
from constants.messages import WELCOME_MESSAGE
from constants.keyboards import MAIN_MENU_KEYBOARD


@Client.on_message(filters.command('start'))
async def start(client: Client, message: Message):
    chat_id = message.chat.id
    username = message.from_user.username

    current_jalali_date = datetime.now()
    formatted_date = current_jalali_date.strftime('%Y/%m/%d')

    if not await is_joined_filter(client, message):
        return

    try:
        user = User.get(User.chat_id == chat_id)
    except User.DoesNotExist:
        user = User.create(
            chat_id=chat_id,
            username=username,
            joined_at=formatted_date,
            coins=str(0),
            invited_users=str(0),
        )

    await client.send_message(
        chat_id=chat_id,
        text=WELCOME_MESSAGE,
        reply_markup=MAIN_MENU_KEYBOARD
    )
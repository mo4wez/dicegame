from pyrogram import Client, filters
from pyrogram.types import Message
from constants.keyboards import JOIN_TO_CHANNEL_KEYBOARD
from constants.messages import FORCE_JOIN_MESSAGE

async def is_user_joined(_, client: Client, message: Message):
    chat_id = message.chat.id
    try:
        user = await client.get_chat_member(
            chat_id="dicegametestpy",
            user_id=message.chat.id,
        )
        if (not user.status == "left" or user.status == "kicked"):
            return True
    except Exception:
        await client.send_message(
            chat_id=chat_id,
            text=FORCE_JOIN_MESSAGE,
            reply_markup=JOIN_TO_CHANNEL_KEYBOARD
        )
        return False

is_joined_filter = filters.create(is_user_joined)
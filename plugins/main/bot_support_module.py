from pyrogram import Client, filters
from pyrogram.types import Message

from constants.messages import BOT_SUPPORT_TEXT

@Client.on_message(filters.regex(BOT_SUPPORT_TEXT))
async def bot_support(client: Client, message: Message):
    chat_id = message.chat.id

    await client.send_message(
        chat_id=chat_id,
        text=BOT_SUPPORT_TEXT,
    )

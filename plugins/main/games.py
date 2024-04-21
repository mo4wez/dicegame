from pyrogram import Client, filters
from pyrogram.types import Message

from constants.messages import (
    PLAY_GAME_TEXT,
    WHICH_GAME_DO_YOU_PLAY,
    )
from constants.keyboards import GAMES_KEYBOARD

@Client.on_message(filters.text & filters.regex(PLAY_GAME_TEXT))
async def show_games_list(client: Client, message: Message):
    chat_id = message.chat.id

    await client.send_message(
        chat_id=chat_id,
        text=WHICH_GAME_DO_YOU_PLAY,
        reply_markup=GAMES_KEYBOARD,
    )
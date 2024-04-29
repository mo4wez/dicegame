from pyrogram import Client, filters
from pyrogram.types import Message

from constants.messages import TRANSFORM_COINS_TEXT


# transform coins
@Client.on_message(filters.regex(TRANSFORM_COINS_TEXT))
async def transform_coins(client: Client, message: Message):
    pass
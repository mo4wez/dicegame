from pyrogram import Client, filters
from pyrogram.types import Message
from jdatetime import datetime
from constants.messages import USER_ACCOUNT_TEXT, USER_INFORMATION_TEXT
from models.users import User

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
from pyrogram import Client, filters
from pyrogram.types import Message
from models.users import User, Invitation
from jdatetime import datetime
from custom_filters.join_checker_filter import is_joined_filter
from constants.messages import (
    WELCOME_MESSAGE,
    YOU_CANT_INVITE_YOURSELF,
    A_USER_SENT_300_COINS,
    YOU_ALREADY_GET_COINS,
    INVALID_INVITE_LINK,
    )
from constants.keyboards import MAIN_MENU_KEYBOARD

from .main.increase_inventory_module import generate_refferal_link


@Client.on_message(filters.command('start'))
async def start(client: Client, message: Message):
    chat_id = message.chat.id
    username = message.from_user.username if message.from_user.username else message.from_user.first_name
    start_text = message.command[1] if len(message.command) > 1 else None

    if not await is_joined_filter(client, message):
        return
    
    if start_text:
        try:
            inviter = User.get(User.invite_link == start_text)

            if not Invitation.select().where(Invitation.inviter == inviter, Invitation.invited_user == chat_id).exists():
                if inviter.chat_id != str(chat_id):
                    inviter_coins = int(inviter.coins)
                    inviter_coins += 300
                    inviter.coins = str(inviter_coins)
                    inviter.save()
                    Invitation.create(inviter=inviter, invited_user=chat_id)
                    await client.send_message(
                        chat_id=inviter.chat_id,
                        text=A_USER_SENT_300_COINS
                    )
                    await client.send_message(
                        chat_id=chat_id,
                        text=WELCOME_MESSAGE.format(username),
                        reply_markup=MAIN_MENU_KEYBOARD
                    )
                else:
                    await client.send_message(
                        chat_id=chat_id,
                        text=YOU_CANT_INVITE_YOURSELF,
                    )
            else:
                await client.send_message(
                    chat_id=chat_id,
                    text=YOU_ALREADY_GET_COINS
                )
        except User.DoesNotExist:
            await client.send_message(
                chat_id=chat_id,
                text=INVALID_INVITE_LINK
            )
    else:
        current_jalali_date = datetime.now()
        formatted_date = current_jalali_date.strftime('%Y/%m/%d')

        try:
            user = User.get(User.chat_id==str(chat_id))
        except User.DoesNotExist:
            user = User.create(
                chat_id=chat_id,
                username=username,
                joined_at=formatted_date,
                invite_link=generate_refferal_link(8),
                coins=str(0),
                invited_users=str(0),
            )
            
        await client.send_message(
            chat_id=chat_id,
            text=WELCOME_MESSAGE.format(username),
            reply_markup=MAIN_MENU_KEYBOARD
            )
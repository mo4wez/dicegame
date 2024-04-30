from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen, Client
from models.users import User, BetResolved
from constants.messages import (
    BET_AMOUNT_QUESTION_TEXT,
    VALID_BET_AMOUNT_TEXT,
    COINS_NOT_ENOUGH,
    BACK_TEXT,
    RETURNED_TO_MAIN_MENU_TEXT,
    DONT_SEND_INVALID_INPUT,
    )
from constants.keyboards import BACK_KEYBOARD, MAIN_MENU_KEYBOARD, DICE_GAME_KEYBOARD


async def dice_game_check(client: Client, message: Message, text_message, game_keyboard):
    chat_id = message.chat.id

    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    bet_resolved_entry.resolved = False
    bet_resolved_entry.save()
    
    try:
        user = User.get(User.chat_id == chat_id)
        bet_amount = await client.ask(
            chat_id=chat_id,
            text=BET_AMOUNT_QUESTION_TEXT.format(user.coins),
            reply_markup=BACK_KEYBOARD
            )

        while True:
            if bet_amount.text == BACK_TEXT:
                print(bet_amount.text)
                await client.send_message(
                    chat_id=chat_id,
                    text=RETURNED_TO_MAIN_MENU_TEXT,
                    reply_markup=MAIN_MENU_KEYBOARD
                )
                break
            if not bet_amount.text.isdigit():
                print(bet_amount.text)
                bet_amount = await client.ask(chat_id, text=DONT_SEND_INVALID_INPUT)
                continue
            if not 100 <= int(bet_amount.text) <= 10000:
                print(bet_amount.text)
                bet_amount = await client.ask(chat_id, text=VALID_BET_AMOUNT_TEXT)
                continue
            if int(bet_amount.text) > int(user.coins):
                print(bet_amount.text)
                await client.send_message(
                    chat_id=chat_id,
                    text=COINS_NOT_ENOUGH,
                    reply_markup=MAIN_MENU_KEYBOARD
                )
                break
            await client.send_message(
                chat_id=chat_id,
                text=text_message,
                reply_markup=game_keyboard
            )
            break
        return bet_amount, user
    except User.DoesNotExist:
        await client.send_message(
            chat_id=chat_id,
            text='Error in getting user.'
        )
from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen, Client
from models.users import BetResolved

from constants.messages import (
    SLOT_GAME_INFO_TEXT,
    SLOTMACHINE_GAME_TEXT,
    MAIN_CHANNEL_ID_TEXT,
    DO_BET,
    YOU_WIN,
    YOU_LOSE,
    SLOT_GAME_WIN_TEXT,
    SLOT_GAME_LOSE_TEXT,
)
from constants.keyboards import MAIN_MENU_KEYBOARD, SLOT_MACHINE_GAME_KEYBOARD
from ..check_bet_module import dice_game_check

@Client.on_message(filters.regex(SLOTMACHINE_GAME_TEXT))
async def slot_game_start(client: Client, message: Message):
    print('in slot game start')
    global bet_amount, user
    bet_amount, user = await dice_game_check(
        client,
        message,
        text_message=SLOT_GAME_INFO_TEXT,
        game_keyboard=SLOT_MACHINE_GAME_KEYBOARD
    )

@Client.on_message(filters.regex(DO_BET))
async def slot_game(client: Client, message: Message):
    chat_id = message.chat.id
    channel_id = 'dicegametestpy'
    user_first_name = message.from_user.first_name
    message_text = message.text

    # Check if bet is already resolved
    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    if bet_resolved_entry.resolved:
        return

    if message_text == DO_BET:
        slot_dice = await client.send_dice(
            chat_id=channel_id,
            emoji='🎰'
        )
        # {'bar': 1, 'grape': 22, 'lemon': 43, 'seven': 64}
        if slot_dice == 1 or slot_dice == 22 or slot_dice == 43 or slot_dice == 64:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 7
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    slot_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=SLOT_GAME_WIN_TEXT.format(
                    chat_id,
                    user_first_name,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=slot_dice.id
            )
        else:
            user.coins = int(user.coins) - int(bet_amount.text)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_LOSE.format(
                    MAIN_CHANNEL_ID_TEXT,
                    slot_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=SLOT_GAME_LOSE_TEXT.format(
                    chat_id,
                    user_first_name,
                    bet_amount.text,
                    str(0)
                ),
                reply_to_message_id=slot_dice.id
            )
    bet_resolved_entry.resolved = True
    bet_resolved_entry.save()
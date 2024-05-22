from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen, Client
from models.users import BetResolved

from constants.messages import (
    DART_GAME_TEXT,
    DART_GAME_INFO_TEXT,
    DART_GAME_HITS,
    DART_GAME_NOT_HITS,
    DART_GAME_RED,
    DART_GAME_WHITE,
    YOU_WIN,
    YOU_LOSE,
    DART_GAME_WIN_MESSAGE,
    DART_GAME_LOSE_MESSAGE,
    DART_GAME_NOT_HIT_WIN_MESSAGE,
    MAIN_CHANNEL_ID_TEXT
)
from constants.keyboards import MAIN_MENU_KEYBOARD, DART_GAME_KEYBOARD
from ..check_bet_module import dice_game_check

@Client.on_message(filters.regex(DART_GAME_TEXT))
async def dart_game_start(client: Client, message: Message):
    global bet_amount, user
    bet_amount, user = await dice_game_check(
        client,
        message,
        text_message=DART_GAME_INFO_TEXT,
        game_keyboard=DART_GAME_KEYBOARD
    )

@Client.on_message(filters.regex(DART_GAME_HITS) | filters.regex(DART_GAME_NOT_HITS) | filters.regex(DART_GAME_RED) | filters.regex(DART_GAME_WHITE))
async def dart_game(client: Client, message: Message):
    chat_id = message.chat.id
    message_text = message.text
    channel_id = 'dicegametestpy'
    user_first_name = message.from_user.username

    # Check if bet is already resolved
    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    if bet_resolved_entry.resolved:
        return

    dart_dice = await client.send_dice(
        chat_id=channel_id,
        emoji='🎯'
    )
    dice_value = dart_dice.dice.value
    
    # 1: out, 2: red ,3: white, 4: red, 5: white, 6: center
    if message_text == DART_GAME_HITS and dice_value == 6:
        user.coins = int(user.coins) - int(bet_amount.text)
        bet_win_coins = int(bet_amount.text) * 3.5
        user.coins = int(user.coins) + int(bet_win_coins)
        user.save()
        await client.send_message(
            chat_id=chat_id,
            text=YOU_WIN.format(
                MAIN_CHANNEL_ID_TEXT,
                dart_dice.id
            ),
            reply_markup=MAIN_MENU_KEYBOARD
        )
        await client.send_message(
            chat_id=channel_id,
            text=DART_GAME_WIN_MESSAGE.format(
                chat_id,
                user_first_name,
                DART_GAME_HITS,
                'وسط',
                bet_amount.text,
                bet_win_coins
            ),
            reply_to_message_id=dart_dice.id
        )
    elif message_text == DART_GAME_NOT_HITS and dice_value == 1:
        user.coins = int(user.coins) - int(bet_amount.text)
        bet_win_coins = int(bet_amount.text) * 3.5
        user.coins = int(user.coins) + int(bet_win_coins)
        user.save()
        await client.send_message(
            chat_id=chat_id,
            text=YOU_WIN.format(
                MAIN_CHANNEL_ID_TEXT,
                dart_dice.id
            ),
            reply_markup=MAIN_MENU_KEYBOARD
        )
        await client.send_message(
            chat_id=channel_id,
            text=DART_GAME_NOT_HIT_WIN_MESSAGE.format(
                chat_id,
                user_first_name,
                DART_GAME_NOT_HITS,
                bet_amount.text,
                bet_win_coins
            ),
            reply_to_message_id=dart_dice.id
        )
    elif message_text == DART_GAME_RED and (dice_value == 2 or dice_value == 4 and not dice_value == 6):
        user.coins = int(user.coins) - int(bet_amount.text)
        bet_win_coins = int(bet_amount.text) * 2
        user.coins = int(user.coins) + int(bet_win_coins)
        user.save()
        await client.send_message(
            chat_id=chat_id,
            text=YOU_WIN.format(
                MAIN_CHANNEL_ID_TEXT,
                dart_dice.id
            ),
            reply_markup=MAIN_MENU_KEYBOARD
        )
        await client.send_message(
            chat_id=channel_id,
            text=DART_GAME_WIN_MESSAGE.format(
                chat_id,
                user_first_name,
                DART_GAME_RED,
                DART_GAME_RED,
                bet_amount.text,
                bet_win_coins
            ),
            reply_to_message_id=dart_dice.id
        )

    elif message_text == DART_GAME_WHITE and (dice_value == 3 or dice_value == 5):
        user.coins = int(user.coins) - int(bet_amount.text)
        bet_win_coins = int(bet_amount.text) * 2
        user.coins = int(user.coins) + int(bet_win_coins)
        user.save()
        await client.send_message(
            chat_id=chat_id,
            text=YOU_WIN.format(
                MAIN_CHANNEL_ID_TEXT,
                dart_dice.id
            ),
            reply_markup=MAIN_MENU_KEYBOARD
        )
        await client.send_message(
            chat_id=channel_id,
            text=DART_GAME_WIN_MESSAGE.format(
                chat_id,
                user_first_name,
                DART_GAME_WHITE,
                DART_GAME_WHITE,
                bet_amount.text,
                bet_win_coins
            ),
            reply_to_message_id=dart_dice.id
        )
    else:
        user.coins = int(user.coins) - int(bet_amount.text)
        user.save()
        await client.send_message(
            chat_id=chat_id,
            text=YOU_LOSE.format(
                MAIN_CHANNEL_ID_TEXT,
                dart_dice.id
            ),
            reply_markup=MAIN_MENU_KEYBOARD
        )
        await client.send_message(
            chat_id=channel_id,
            text=DART_GAME_LOSE_MESSAGE.format(
                chat_id,
                user_first_name,
                message_text,
                bet_amount.text,
                str(0)
            ),
            reply_to_message_id=dart_dice.id
        )
    bet_resolved_entry.resolved = True
    bet_resolved_entry.save()

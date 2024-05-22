from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen, Client
from models.users import BetResolved
from ..check_bet_module import dice_game_check
from constants.messages import (
    FUTBALL_GAME_TEXT,
    FUTBALL_GAME_INFO,
    FUTBALL_GAME_ITS_GOAL,
    FUTBALL_GAME_ITS_NOT_GOAL,
    MAIN_CHANNEL_ID_TEXT,
    YOU_WIN,
    YOU_LOSE,
    FUTBALL_GAME_WIN_MESSAGE,
    FUTBALL2_GAME_WIN_MESSAGE,
    FUTBALL_GAME_LOSE_MESSAGE,
)
from constants.keyboards import FUTBALL_GAME_KEYBOARD, MAIN_MENU_KEYBOARD

@Client.on_message(filters.regex(FUTBALL_GAME_TEXT))
async def futball_game_start(client: Client, message: Message):
    global bet_amount, user
    bet_amount, user = await dice_game_check(client, message, text_message=FUTBALL_GAME_INFO, game_keyboard=FUTBALL_GAME_KEYBOARD)

@Client.on_message(filters.regex(FUTBALL_GAME_ITS_GOAL) | filters.regex(FUTBALL_GAME_ITS_NOT_GOAL))
async def futball_game(client: Client, message: Message):
    chat_id = message.chat.id
    message_text = message.text
    channel_id = 'dicegametestpy'
    user_first_name = message.from_user.first_name

    # Check if bet is already resolved
    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    if bet_resolved_entry.resolved:
        return

    # 1: out, 2: post, 3: goal, 4: goal, 5: goal, 6:
    if message_text == FUTBALL_GAME_ITS_GOAL:
        goals = 0
        for _ in range(2):
            futball_dice = await client.send_dice(
                chat_id=channel_id,
                emoji='⚽️',
            )
            dice_value = futball_dice.dice.value

            if dice_value == 4 or dice_value == 5:
                goals += 1

        if goals == 2:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 2
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    futball_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=FUTBALL_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    FUTBALL_GAME_ITS_GOAL,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=futball_dice.id
            )
        else:
            user.coins = int(user.coins) - int(bet_amount.text)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_LOSE.format(
                    MAIN_CHANNEL_ID_TEXT,
                    futball_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=FUTBALL_GAME_LOSE_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    FUTBALL_GAME_ITS_GOAL,
                    bet_amount.text,
                    str(0)
                ),
                reply_to_message_id=futball_dice.id
            )

    if message_text == FUTBALL_GAME_ITS_NOT_GOAL:
        missed_balls = 0
        for _ in range(2):
            futball_dice = await client.send_dice(
                chat_id=channel_id,
                emoji='⚽️'
            )
            dice_value = futball_dice.dice.value

            if not dice_value == 4 and not dice_value == 5:
                missed_balls += 1
            print(f'missed: {missed_balls}')

        if missed_balls == 2:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 2
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    futball_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=FUTBALL2_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    FUTBALL_GAME_ITS_NOT_GOAL,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=futball_dice.id
            )
        else:
            user.coins = int(user.coins) - int(bet_amount.text)
            user.save()

            await client.send_message(
                chat_id=chat_id,
                text=YOU_LOSE.format(
                    MAIN_CHANNEL_ID_TEXT,
                    futball_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=FUTBALL_GAME_LOSE_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    FUTBALL_GAME_ITS_NOT_GOAL,
                    bet_amount.text,
                    str(0)      
                ),
                reply_to_message_id=futball_dice.id
            )
    bet_resolved_entry.resolved = True
    bet_resolved_entry.save()
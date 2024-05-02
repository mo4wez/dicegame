from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen, Client
from models.users import BetResolved

from constants.messages import (
    BASKETBALL_GAME_TEXT,
    BASKETBALL_GAME_INFO,
    ITS_GOAL,
    ITS_NOT_GOAL,
    YOU_WIN,
    YOU_LOSE,
    BASKETBALL_GAME_WIN_MESSAGE,
    BASKETBALL_GAME_LOSE_MESSAGE,
    MAIN_CHANNEL_ID_TEXT,
    BASKETBALL2BALL_GAME_WIN_MESSAGE,
)
from constants.keyboards import BASKETBAL_GAME_KEYBOARD, MAIN_MENU_KEYBOARD
from .check_bet_module import dice_game_check

@Client.on_message(filters.regex(BASKETBALL_GAME_TEXT))
async def basketball_game_start(client: Client, message: Message):
    global bet_amount, user
    bet_amount, user = await dice_game_check(client, message, text_message=BASKETBALL_GAME_INFO, game_keyboard=BASKETBAL_GAME_KEYBOARD)

@Client.on_message(filters.regex(ITS_GOAL) | filters.regex(ITS_NOT_GOAL))
async def basketball_game(client: Client, message: Message):
    chat_id = message.chat.id
    message_text = message.text
    channel_id = 'dicegametestpy'
    user_first_name = message.from_user.first_name

    # Check if bet is already resolved
    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    if bet_resolved_entry.resolved:
        return


    if message_text == ITS_GOAL:
        basketball_dice = await client.send_dice(
            chat_id=channel_id,
            emoji='🏀'
        )
        if basketball_dice.dice.value == 4 or basketball_dice.dice.value == 5:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 2
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    basketball_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BASKETBALL_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    ITS_GOAL,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=basketball_dice.id
            )
        else:
            user.coins = int(user.coins) - int(bet_amount.text)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_LOSE.format(
                    MAIN_CHANNEL_ID_TEXT,
                    basketball_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BASKETBALL_GAME_LOSE_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    ITS_GOAL,
                    bet_amount.text,
                    str(0)
                ),
                reply_to_message_id=basketball_dice.id
            )
    if message_text == ITS_NOT_GOAL:
        dice_values = []
        for _ in range(1,3):
            basketball_dice = await client.send_dice(
                chat_id=channel_id,
                emoji='🏀'
            )
            dice_values.append(basketball_dice.dice.value)
        if not dice_values[0] == 4 and not dice_values[1] == 4 and not dice_values[0] == 5 and not dice_values[1] == 5:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 2
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    basketball_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BASKETBALL2BALL_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    ITS_NOT_GOAL,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=basketball_dice.id
            )
        else:
            await client.send_message(
                chat_id=chat_id,
                text=YOU_LOSE.format(
                    MAIN_CHANNEL_ID_TEXT,
                    basketball_dice.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            user.coins = int(user.coins) - int(bet_amount.text)
            user.save()
            await client.send_message(
                chat_id=channel_id,
                text=BASKETBALL_GAME_LOSE_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    ITS_NOT_GOAL,
                    bet_amount.text,
                    str(0)
                ),
                reply_to_message_id=basketball_dice.id
            )
    bet_resolved_entry.resolved = True
    bet_resolved_entry.save()




from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen, Client
from models.users import BetResolved
from constants.messages import (
    BOWLING_GAME_TEXT,
    BOWLING_GAME_INFO,
    BOWLING_GAME_0,
    BOWLING_GAME_1,
    BOWLING_GAME_3,
    BOWLING_GAME_4,
    BOWLING_GAME_5,
    BOWLING_GAME_6,
    BOWLING_GAME_WIN_MESSAGE,
    BOWLING_GAME_LOSE_MESSAGE,
    YOU_WIN,
    YOU_LOSE,
    MAIN_CHANNEL_ID_TEXT,
)
from constants.keyboards import MAIN_MENU_KEYBOARD, BOWLING_GAME_KEYBOARD
from ..check_bet_module import dice_game_check

@Client.on_message(filters.regex(BOWLING_GAME_TEXT))
async def bowling_game_start(client: Client, message: Message):
    global bet_amount, user
    bet_amount, user = await dice_game_check(client, message, text_message=BOWLING_GAME_INFO, game_keyboard=BOWLING_GAME_KEYBOARD)


@Client.on_message(filters.regex(BOWLING_GAME_0) | filters.regex(BOWLING_GAME_1) | filters.regex(BOWLING_GAME_3) | filters.regex(BOWLING_GAME_4) | filters.regex(BOWLING_GAME_5) | filters.regex(BOWLING_GAME_6))
async def bowling_game(client: Client, message: Message):
    chat_id = message.chat.id
    message_text = message.text
    channel_id = 'dicegametestpy'
    user_first_name = message.from_user.first_name

    # Check if bet is already resolved
    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    if bet_resolved_entry.resolved:
        return

    boling_text = await client.send_dice(
        chat_id=channel_id,
        emoji='🎳',
    )

    if message_text == BOWLING_GAME_0 and boling_text.dice.value == 1:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 4.5
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    boling_text.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BOWLING_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    BOWLING_GAME_0,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=boling_text.id
            )
    elif message_text == BOWLING_GAME_1 and boling_text.dice.value == 2:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 4.5
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    boling_text.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BOWLING_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    BOWLING_GAME_1,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=boling_text.id
            )
    elif message_text == BOWLING_GAME_3 and boling_text.dice.value == 3:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 4.5
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    boling_text.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BOWLING_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    BOWLING_GAME_3,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=boling_text.id
            )
    elif message_text == BOWLING_GAME_4 and boling_text.dice.value == 4:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 4.5
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    boling_text.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BOWLING_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    BOWLING_GAME_0,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=boling_text.id
            )
    elif message_text == BOWLING_GAME_5 and boling_text.dice.value == 5:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 4.5
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    boling_text.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BOWLING_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    BOWLING_GAME_5,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=boling_text.id
            )
    elif message_text == BOWLING_GAME_6 and boling_text.dice.value == 6:
            user.coins = int(user.coins) - int(bet_amount.text)
            bet_win_coins = int(bet_amount.text) * 4.5
            user.coins = int(user.coins) + int(bet_win_coins)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN.format(
                    MAIN_CHANNEL_ID_TEXT,
                    boling_text.id
                ),
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=BOWLING_GAME_WIN_MESSAGE.format(
                    chat_id,
                    user_first_name,
                    BOWLING_GAME_6,
                    bet_amount.text,
                    bet_win_coins
                ),
                reply_to_message_id=boling_text.id
            )
    else:
        user.coins = int(user.coins) - int(bet_amount.text)
        user.save()
        await client.send_message(
            chat_id=chat_id,
            text=YOU_LOSE.format(
                MAIN_CHANNEL_ID_TEXT,
                boling_text.id
            ),
            reply_markup=MAIN_MENU_KEYBOARD
        )
        await client.send_message(
            chat_id=channel_id,
            text=BOWLING_GAME_LOSE_MESSAGE.format(
                chat_id,
                user_first_name,
                message_text,
                bet_amount.text,
                str(0),
            ),
            reply_to_message_id=boling_text.id
        )
    bet_resolved_entry.resolved = True
    bet_resolved_entry.save()
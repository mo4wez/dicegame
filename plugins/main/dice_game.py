from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen, Client
from models.users import User, BetResolved
from constants.messages import (
    DICE_GAME_TEXT,
    BET_AMOUNT_QUESTION_TEXT,
    DICE_GAME_INFO,
    VALID_BET_AMOUNT_TEXT,
    COINS_NOT_ENOUGH,
    BACK_TEXT,
    RETURNED_TO_MAIN_MENU_TEXT,
    DONT_SEND_INVALID_INPUT,
    DICE_BET_ON_EVEN,
    DICE_BET_ON_ODD,
    NUMBERS_STR_LIST,
    DICE_GAME_EVEN_BET_WIN_TEXT,
    DICE_GAME_EVEN_BET_LOSE_TEXT,
    DICE_GAME_ODD_BET_LOSE_TEXT,
    DICE_GAME_ODD_BET_WIN_TEXT,
    DICE_GAME_NUMBERS_BET_WIN,
    DICE_GAME_NUMBERS_BET_LOSE,
    YOU_LOSE,
    YOU_WIN,
    MAIN_CHANNEL_LINK_TEXT,
    )
from constants.keyboards import BACK_KEYBOARD, MAIN_MENU_KEYBOARD, DICE_GAME_KEYBOARD

@Client.on_message(filters.regex(DICE_GAME_TEXT))
async def dice_game(client: Client, message: Message):
    chat_id = message.chat.id

    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    bet_resolved_entry.resolved = False
    bet_resolved_entry.save()
    
    try:
        global user
        global bet_amount
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
            user.coins = int(user.coins) - int(bet_amount.text)
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=DICE_GAME_INFO,
                reply_markup=DICE_GAME_KEYBOARD
            )
            break
    except User.DoesNotExist:
        await client.send_message(
            chat_id=chat_id,
            text='Error in getting user.'
        )


@Client.on_message(filters.regex(DICE_BET_ON_EVEN) | filters.regex(DICE_BET_ON_ODD))
async def bet_odd_or_even(client: Client, message: Message):
    global last_dice_text
    chat_id = message.chat.id
    message_text = message.text
    channel_id = 'dicegametestpy'
    user_first_name = message.from_user.first_name

    # Check if bet is already resolved
    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    if bet_resolved_entry.resolved:
        return
    
    dice_values = []
    if message_text == DICE_BET_ON_EVEN:
        for _ in range(1,3):
            dice_text = await client.send_dice(
                chat_id=channel_id,
                emoji='🎲',   
            )
            dice_values.append(dice_text.dice.value)
        print(dice_text)

        if dice_values[0] % 2 == 0 and dice_values[1] % 2 == 0:
            bet_win_coins = int(bet_amount.text) * 2
            user.coins = int(user.coins) + bet_win_coins
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN,
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=DICE_GAME_EVEN_BET_WIN_TEXT.format(
                    chat_id,
                    user_first_name,
                    bet_amount.text,
                    str(bet_win_coins)
                ),
                reply_to_message_id=dice_text.id
            )
        else:
            await client.send_message(
                chat_id=chat_id,
                text=YOU_LOSE,
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=DICE_GAME_EVEN_BET_LOSE_TEXT.format(
                    chat_id,
                    user_first_name,
                    bet_amount.text, 
                    str(0)
                ),
                reply_to_message_id=dice_text.id
            )
        
        bet_resolved_entry.resolved = True
        bet_resolved_entry.save()

    if message_text == DICE_BET_ON_ODD:
        for _ in range(1,3):
            dice_text = await client.send_dice(
                chat_id=channel_id,
                emoji='🎲',   
            )
            dice_values.append(dice_text.dice.value)

        if not dice_values[0] % 2 == 0 and not dice_values[1] % 2 == 0:
            bet_win_coins = int(bet_amount.text) * 2
            user.coins = int(user.coins) + bet_win_coins
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN,
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=DICE_GAME_ODD_BET_WIN_TEXT.format(
                    chat_id,
                    user_first_name,
                    bet_amount.text,
                    str(bet_win_coins),
                ),
                reply_to_message_id=dice_text.id
            )
        else:
            await client.send_message(
                chat_id=chat_id,
                text=YOU_LOSE,
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=DICE_GAME_ODD_BET_LOSE_TEXT.format(
                    chat_id,
                    user_first_name,
                    bet_amount.text,
                    str(0),
                ),
                reply_to_message_id=dice_text.id
            )
        bet_resolved_entry.resolved = True
        bet_resolved_entry.save()

pattern = r'^[1-6]$'
@Client.on_message(filters.regex(pattern))
async def bet_on_numbers(client: Client, message: Message):
    global bet_resolved
    chat_id = message.chat.id
    message_text = message.text
    user_first_name = message.from_user.first_name
    channel_id = 'dicegametestpy'

    # Check if bet is already resolved
    bet_resolved_entry, created = BetResolved.get_or_create(chat_id=chat_id, defaults={'resolved': False})
    if bet_resolved_entry.resolved:
        return

    if message_text == BACK_TEXT:
        print(message_text)
        await client.send_message(
            chat_id=chat_id,
            text=RETURNED_TO_MAIN_MENU_TEXT,
            reply_markup=MAIN_MENU_KEYBOARD
        )
    if message_text in NUMBERS_STR_LIST:
        dice_text = await client.send_dice(
                chat_id='dicegametestpy',
                emoji='🎲',
            )
        if message_text == str(dice_text.dice.value):
            bet_win_coins = int(bet_amount.text) * 4
            user.coins = int(user.coins) + bet_win_coins
            user.save()
            await client.send_message(
                chat_id=chat_id,
                text=YOU_WIN,
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=DICE_GAME_NUMBERS_BET_WIN.format(
                    chat_id,
                    user_first_name,
                    message_text,
                    message_text,
                    bet_amount.text,
                    str(bet_win_coins)
                ),
                reply_to_message_id=dice_text.id
            )
        else:
            await client.send_message(
                chat_id=chat_id,
                text=YOU_LOSE,
                reply_markup=MAIN_MENU_KEYBOARD
            )
            await client.send_message(
                chat_id=channel_id,
                text=DICE_GAME_NUMBERS_BET_LOSE.format(
                    chat_id,
                    user_first_name,
                    message_text,
                    message_text,
                    bet_amount.text,
                    str(0)
                ),
                reply_to_message_id=dice_text.id
            )
        bet_resolved_entry.resolved = True
        bet_resolved_entry.save()
       
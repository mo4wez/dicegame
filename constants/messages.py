# force join message
FORCE_JOIN_MESSAGE = '''
کاربر {} عزیز

⚠️ جهت ادامه کار نیاز است در کانال نیتروسین بت عضو شوید.
@dicegametestbot

👈🏻 بعد از عضویت مجددا /start را ارسال نمایید.
'''
# channel link
MAIN_CHANNEL_ID_TEXT = 'dicegametestpy'
MAIN_CHANNEL_LINK_TEXT = 'https://t.me/dicegametestpy'
# welcome message
WELCOME_MESSAGE = '''
سلام {}،به دایس گیم تست بت خوش آمدید 💫

👈🏻 با دایس گیم تست بت میتوانید سکه های دایس گیم خود را کاملا اتومات چند برابر کنید😍😍
برای ادامه یکی از دکمه های زیر را انتخاب نمایید:
'''

# numbers
NUMBERS_STR_LIST = ['1', '2', '3', '4', '5', '6']

# cancel
CANCEL_TEXT = 'انصراف'

# back
BACK_TEXT = '🔙 بازگشت'
RETURNED_TO_MAIN_MENU_TEXT = '👈🏻 به منوی اصلی بازگشتید.'

# main menu buttons text
PLAY_GAME_TEXT = '🎮شروع بازی'
TRANSFORM_COINS_TEXT = '💸انتقال سکه'
USER_ACCOUNT_TEXT = '👤حساب کاربری'
SUPPORT_TEXT = '🆘 پشتیبانی'
INCREASE_INVENTORY_TEXT = '➕ افزایش موجودی'
BOOK_ICON_TEXT = '📖'

# games text and messages
WHICH_GAME_DO_YOU_PLAY = '🎮روی کدوم بازی میخوای شرط ببندی؟👇'
DICE_GAME_TEXT = 'تاس 🎲'
BOWLING_GAME_TEXT = 'بولینگ 🎳'
BASKETBALL_GAME_TEXT = 'بسکتبال 🏀'
FUTBALL_GAME_TEXT = 'فوتبال ⚽️'
DART_GAME_TEXT = 'دارت 🎯'
SLOTMACHINE_GAME_TEXT = 'ماشین اسلات 🎰'

DICE_GAME_INFO = '''
🎲بازی تاس:

1.شما میتوانید روی زوج یا فرد آمادن شرط ببندید که در این صورت دوتاس انداخته میشود که باید هر دوتا با توجه به شرط یا زوج بیاید یا فرد.(ضریب: 2)

2.میتوانید روی اعداد شرط ببندید که یک تاس انداخته میشود اگر عدد شرط شما آمد شما برنده اید.(ضریب: 4)
'''
DICE_BET_ON_EVEN = 'شرط روی زوج'
DICE_BET_ON_ODD = 'شرط روی فرد'

# dice game button messages and texts
BET_AMOUNT_QUESTION_TEXT = '''
👈🏻سر چقدر سکه شرط میبندی؟

• موجودی شما: {} سکه
'''

# coins not enough
COINS_NOT_ENOUGH = '❗️موجودی شما کافی نیست!'

# send valid coins amount
DONT_SEND_INVALID_INPUT = 'لطفا برای تعداد سکه ها فقط عدد ارسال کنید'

# you win / lose
YOU_WIN = "<a href='https://t.me/{}/{}'>😄بردی😄</a>"
YOU_LOSE = "<a href='https://t.me/{}/{}'>😞باختی😞</a>"
DICE_GAME_ODD_BET_LOSE_TEXT = '''
👤کاربر {}-{}

💵شرط: شرط روی فرد 
❌شرط جدیدی انجام داد و باخت و هر دو تاس فرد نشد.
💰سکه شرط: {}
🎁پاداش: {}
'''
DICE_GAME_ODD_BET_WIN_TEXT = '''
👤کاربر {}-{}

💵شرط: شرط روی فرد 
✅شرط جدیدی انجام داد و برد و هر دو تاس فرد شد.
💰سکه شرط: {}
🎁پاداش: {}
'''
DICE_GAME_EVEN_BET_WIN_TEXT = '''
👤کاربر {}-{}

💵شرط:شرط روی زوج
✅شرط جدیدی انجام داد و برد و هر دو تاس زوج شد.
💰سکه شرط: {}
🎁پاداش: {}
'''
DICE_GAME_EVEN_BET_LOSE_TEXT = '''
👤کاربر {}-{}

💵شرط:شرط روی زوج
❌شرط جدیدی انجام داد و باخت و هر دو تاس زوج نشد.
💰سکه شرط: {}
🎁پاداش: {}
'''
DICE_GAME_NUMBERS_BET_WIN = '''
👤کاربر {}-{}

💵شرط:{}
✅شرط جدیدی انجام داد برد و تاس {} شد.
💰سکه شرط: {}
🎁پاداش: {}
'''
DICE_GAME_NUMBERS_BET_LOSE = '''
👤کاربر {}-{}

💵شرط:{}
❌شرط جدیدی انجام داد باخت و تاس {} نشد.
💰سکه شرط: {}
🎁پاداش: {}
'''
# Bowling game message
BOWLING_GAME_INFO = '''
🎳بازی بولینگ:

1.تعداد مانع هایی که میوفتن؟.(ضریب: 4.5)
'''

BOWLING_GAME_0 = 'صفر مانع'
BOWLING_GAME_1 = 'یک مانع'
BOWLING_GAME_3 = 'سه مانع'
BOWLING_GAME_4 = 'چهار مانع'
BOWLING_GAME_5 = 'پنج مانع'
BOWLING_GAME_6 = 'شش مانع'

# Blowling win or lose message
BOWLING_GAME_WIN_MESSAGE = '''
👤کاربر {}-{}

💵شرط: {}
✅شرط جدیدی انجام داد و برد.
💰سکه شرط: {}
🎁پاداش: {}
'''
BOWLING_GAME_LOSE_MESSAGE = '''
👤کاربر {}-{}

💵شرط: {}
❌شرط جدیدی انجام داد و باخت.
💰سکه شرط: {}
🎁پاداش: {}
'''

# Basketball Game text and messages
BASKETBALL_GAME_INFO = '''
🏀بازی بسکتبال:

1.توپ شما وارد حلقه میشود و شرط را میبرید..(ضریب: 2)

2.دو تا توپ انداخته میشود و اگر هر دو گل نشد شما برنده هستید..(ضریب: 2)
'''
ITS_GOAL = 'گل میشود'
ITS_NOT_GOAL = 'گل نمیشود'

BASKETBALL_GAME_LOSE_MESSAGE = '''
👤کاربر {}-{}

💵شرط: {} 
❌شرط جدیدی انجام داد و باخت.
💰سکه شرط: {}
🎁پاداش: {}
'''

BASKETBALL_GAME_WIN_MESSAGE = '''
👤کاربر {}-{}

💵شرط: {}
✅شرط جدیدی انجام داد و برد و پرتاپ گل شد.
💰سکه شرط: {}
🎁پاداش: {}
'''
BASKETBALL2BALL_GAME_WIN_MESSAGE = '''
👤کاربر {}-{}

💵شرط: {}
✅شرط جدیدی انجام داد و برد و هر دو پرتاپ گل نشد.
💰سکه شرط: {}
🎁پاداش: {}
'''
# Football game text and messages
FUTBALL_GAME_INFO = '''
⚽️بازی فوتبال:

1.دوتا توپ در کانال فرستاده میشه باید هر دو گل بشه..(ضریب: 2)

2.دوتا توپ در کانال فرستاده میشه نباید توپی وارد دروازه بشه.(ضریب: 2)
'''
FUTBALL_GAME_ITS_GOAL = 'گل می شود'
FUTBALL_GAME_ITS_NOT_GOAL = 'گل نمی شود'
FUTBALL_GAME_WIN_MESSAGE = '''
👤کاربر {}-{}

💵شرط: {} 
✅شرط جدیدی انجام داد و برد و هردو توپ گل شد.
💰سکه شرط: {}
🎁پاداش: {}
'''
FUTBALL2_GAME_WIN_MESSAGE = '''
👤کاربر {}-{}

💵شرط: {} 
✅شرط جدیدی انجام داد و برد و هردو توپ گل نشد.
💰سکه شرط: {}
🎁پاداش: {}
'''
FUTBALL_GAME_LOSE_MESSAGE = '''
👤کاربر {}-{}

💵شرط: {} 
❌شرط جدیدی انجام داد و باخت.
💰سکه شرط: {}
🎁پاداش: {}
'''

# user account message
USER_INFORMATION_TEXT = '''
👤 شناسه شما: {}
📅 تاریخ عضویت: {}
👥 زیرمجموعه: {} نفر
💰 موجودی شما: {} سکه

@dicegametestbot - {}
'''

VALID_BET_AMOUNT_TEXT = '''
❗️ تعداد سکه انتخابی برای شرط باید بین 100 الی 10000 سکه باشد.
'''

# transform coins message
TRANSFORM_COINS_MESSAGE = '''
❓ تعداد سکه موردنظر جهت انتقال را وارد نمایید:

• موجودی شما: {} سکه
'''
TRANSFORM_INVALID_TEXT = '''
❌ این انتقال قابل انجام نیست! برای انتقال نیاز است که 300 سکه داخل حساب خودتان باقی بماند.!
'''

# increase inventory message and text
INVITE_USER_TEXT = '👤 زیرمجموعه گیری'
TRANSFORM_NITROSEEN_TEXT = '💵 انتقال نیتروسین'
TRANSFORM_NITROSEEN_MESSAGE = '''
برای شارژ حساب خود باید سکه ربات نیتروسین (bot link) را برای کاربری user_id انتقال دهید😊

کاربری: user_id

‼️توجه: بعد از انتقال اتومات حسابی که با آن انتقال دادید شارژ میشه.
'''
INCREASE_INVENTORY_MESSAGE = '''
یک بخش را جهت افزایش موجودی انتخاب کنید:
'''
CONGRATS_300_COINS_RECIVED = '🎈 تبریک، 300 سکه بابت زیرمجموعه جدید دریافت کردید.'


# bot support text
BOT_SUPPORT_TEXT = '''
🔰 تیم پشتیبانی نیتروسین بت با افتخار آماده پاسخگویی به شما عزیزان است:
@moawezz
'''

# bot instruction message
BOT_INSTRUCTION_MESSAGE = '''
👈🏻چگونه حساب خود را شارژ کنم؟
برای شارژ حساب خود کافیست سکه های نیتروسین خود را به کاربری {} انتقال دهید و اتومات بعد از انتقال حساب شما شارژ میشود.

👈🏻بردم،چطور جایزه را دریافت کنم؟
ربات به صورت اتومات بین 1 تا 10 دقیقه بعد از برد شما،جایزه را به حساب کاربری شما انتقال میدهد و برای شما پیام انتقال را ارسال میکند.

👈🏻موجودی دارم چطور برداشت کنم؟
در حال حاضر فقط با بازی کردن و شرط بستن میتوانید سکه نیتروسین بگیرید
'''

# user invite link
USER_INVITE_LINK = 'https://t.me/dicegametestbot?start={}'
INVITE_MESSAGE = '''
⚡️ با نیتروسین بت به راحتی سکه های نیتروسین خود را چند برابر کنید!

🤯کاملا اتومات بعد از انتقال نیترو به کاربری مورد نظر حساب شما در ربات شارژ شده و بعد از بردن اتومات برای شما واریز میشود🤩

📌 همین حالا رایگان امتحان کن👇👇

{}
'''
INVITE_INFO_TEXT = '''
💡 به ازای هر شخصی که برای اولین بار با لینک شما عضو ربات شود 300 سکه دریافت خواهید کرد.
برای شروع بنر بالا را به دوستان و آشنایان خود ارسال کنید.
'''
YOU_CANT_INVITE_YOURSELF = 'نمی تونی با لینک عضوگیری خودت سکه بگیری'
A_USER_SENT_300_COINS = 'با دعوت دوستت 300  سکه به حسابت نشست.'
YOU_ALREADY_GET_COINS = 'با این لینک قبلا سکه گرفتی'
INVALID_INVITE_LINK = 'لینک عضوگیری اشتباهه، با لینک صحیح امتحان کن.'
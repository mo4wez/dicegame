from pyrogram import Client
from bot_config import DiceGameBotConfig
import pyromod
import logging
import configparser

# configure plugins
plugins = dict(root="plugins")

# read .env file
config = DiceGameBotConfig()

api_id = config.api_id
api_hash = config.api_hash
token = config.token

# read proxy file
config = configparser.ConfigParser()
config.read('proxy.ini')

proxy = {
    "scheme": config.get('proxy', 'scheme'),
    "hostname": config.get('proxy', 'hostname'),
    "port": config.getint('proxy', 'port'),
}

# Client instance
bot = Client(
    name="dice_game",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=token,
    plugins=plugins,
    proxy=proxy
)

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    bot.run()
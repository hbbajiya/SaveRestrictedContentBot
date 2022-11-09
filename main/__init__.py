#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID= 1861487
API_HASH= "a27467973862c196b2aac7741c655369"  config("API_HASH", default=None)
BOT_TOKEN= "5022724902:AAFVS_ZPuOpIizmOYsGGzJSTQoBTCqSQ1K0" config("BOT_TOKEN", default=None)
SESSION= "AQCcJXHk3mjo2O-DBRlpQBpAeSFmHktj-xNFGOIj2bQu6Si6bP0BfgMhSQpNs9ViwbAI7ej7WXXgD0uU0Fy4-mLsyXu7cS0Dws8kQjBrs4ZidamiRSzajH9P2qawdVHxpMSRmQ0r_AyV_9BMD6uMZjaTvormbgKcIQ9YeolezqXHtBz8C4AdoGHoMf13KTlD6MxofDV322dAbIH1dcZy0W9FAcEFgJV7-yZYNaWJOGQ8QMyVJnk5upAd2rlrClep98LUOLr1YXaU7ReD31dIcaQw5KIGd6cagCrHMf0M7j0r9h8QCfnlaf-oOz7NX8gwCpPI5mPLDnfMv8q3ZdrWTaskZ0d3_AA " config("SESSION", default=None)
FORCESUB="Dronebots" config("FORCESUB", default=None)
AUTH="906349244,1732737020" config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

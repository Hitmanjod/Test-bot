import os
import time 


class Config(object):
	API_ID = int(os.environ.get("API_ID", "25502576"))
	API_HASH = os.environ.get("API_HASH", "f0f35dbb5b0081cdc8d3c9d5383c4628")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6369183180:AAE8nXrcaNI-ZPMtdn4AxI6Uf99wZ-6BWt0")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "VnshortenerFileStoreBot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001948924720"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5123039648"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://HitmanLaude12:HitmanLaude12@cluster0.logbo9e.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001948924720")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BASE_SITE = os.environ.get("BASE_SITE", "vnshortener.com")
	DOMAIN = os.environ.get("DOMAIN", "vnshortener.com")
	ABOUT_BOT_TEXT = f"""
This is Public Files Store Bot !
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Vn File Store Bot](https://t.me/VnshortenerFileStoreBot)

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

👑 **Owner:** Deleted Account

📢 **Updates Channel:** @Sujan_BotZ 
"""
	ABOUT_DEV_TEXT = f"""
**🌐 This Bot Was Devloped By** : @Sujan_BotZ"""
	
PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
START_MEDIA = "https://graph.org/file/6b16ad03f00948d2d719e.jpg"
START_TEXT = """Hɪ/Hᴇʟʟᴏ [{}](tg://user?id={})

This is a Vnshortener FileStore Bot.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from CopyRight Infringement Issue. I support Channel Also You Can Check About Bot.

❌ PORNOGRAPHY CONTENTS are strictly prohibited & get Permanent Ban.

Pᴏᴡᴇʀᴇᴅ Bʏ : [Sujan_BotZ](http://Sujan_BotZ)"""

HELP_TEXT = """Hᴏᴡ Tᴏ Verify:

Sᴛᴇᴘ Nᴏ 1 : Just Copy Your Api Token From Website.

Sᴛᴇᴘ Nᴏ 2 : Then Use /api Paste Your Api Token Here.

Exᴀᴍᴘʟᴇ : /api ```6c5db31980885e46221e90106f1d47b8295aa0f8``` """

ABOUT_TEXT = """🤖 Name : Vnshortener File Store Bot 

🔠 Language  : Python3
📚 Library   : Teleton And Pyrogram
👑 Owner     : Deleted Account 

©️Powered By @Sujan_BotZ """




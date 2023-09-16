# © Telegram @HMF_Owner_1, GitHub @ThiruXD 

import os
import time 


class Config(object):
	API_ID = int(os.environ.get("API_ID", "25502576"))
	API_HASH = os.environ.get("API_HASH", "f0f35dbb5b0081cdc8d3c9d5383c4628")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6449209866:AAG9QJDwNhJI14rXM2zMVvt7yIO_F8fsphY")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "TG_File_Store_Ro_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001936300025"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5123039648"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://SujanC7:SujanC7@cluster0.vst9zln.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001978535504")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BASE_SITE = os.environ.get("BASE_SITE", "")
	DOMAIN = os.environ.get("DOMAIN", "")
	ABOUT_BOT_TEXT = f"""
This is Public Files Store Bot !
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [File Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

👑 **Owner:** @Sujan_Ch

📢 **Updates Channel:** @Sujan_BotZ 
"""
	ABOUT_DEV_TEXT = f"""
**🌐 This Bot Was Devloped By** : @Sujan_Ch"""
	
PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
START_MEDIA = "https://graph.org/file/a18cf9f447a1c34e5a20a.jpg"
START_TEXT = """Hɪ/Hᴇʟʟᴏ [{}](tg://user?id={})

This is a Permanent FileStore Bot.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from CopyRight Infringement Issue. I support Channel Also You Can Check About Bot.

❌ PORNOGRAPHY CONTENTS are strictly prohibited & get Permanent Ban.

Pᴏᴡᴇʀᴇᴅ Bʏ : [Sujan_Ch](http://Sujan_BotZ)"""

HELP_TEXT = """Hᴏᴡ Tᴏ Verify:

Sᴛᴇᴘ Nᴏ 1 : Just Copy This (6c5db31980885e46221e90106f1d47b8295aa0f8) Token.

Sᴛᴇᴘ Nᴏ 2 : Then Use /verify Paste Token Here.

Exᴀᴍᴘʟᴇ : /verify 6c5db31980885e46221e90106f1d47b8295aa0f8 """

ABOUT_TEXT = """🤖 Name : File Store Bot 

🔠 Language  : Python3
📚 Library   : Teleton And Pyrogram
👑 Owner     : @sujan_ch

©️Powered By @Sujan_BotZ """




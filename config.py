# +++ Made By King [telegram username: @Elites_18] +++

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org, --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", "25120562"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "0bd8eb78385a059f64f6032ebefc4615")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002435149290"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "")

#Port
PORT = os.environ.get("PORT", "8011")

#Database --⚠️ REQUIRED--
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ddcluster6:dsquad@ddcluster6.8stdt.mongodb.net/?retryWrites=true&w=majority&appName=ddCluster6")

DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "20"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://files.catbox.moe/3idqkp.jpg https://files.catbox.moe/o115bv.jpg https://files.catbox.moe/f0p4zk.jpg https://files.catbox.moe/5f4kqv.jpg https://files.catbox.moe/5n2f0n.jpg https://files.catbox.moe/ornbpv.jpg https://files.catbox.moe/kfyxlc.jpg https://files.catbox.moe/tjkzo3.jpg https://files.catbox.moe/7246mu.jpg https://files.catbox.moe/kzt0pp.jpg https://files.catbox.moe/eusb30.jpg https://files.catbox.moe/jwmmvi.jpg https://files.catbox.moe/4tk1fk.jpg")).split() #Required

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

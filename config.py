import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID", "26066227"))  
API_HASH = os.getenv("API_HASH", "ccc671534727ba045306c5d27fde1475")

# Bot Token / String Session
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING1 = os.getenv("STRING_SESSION", None)

# Database
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://pusers:nycreation@nycreation.pd4klp1.mongodb.net/?retryWrites=true&w=majority&appName=NYCREATION")

# Owner / Admin
OWNER_ID = int(os.getenv("OWNER_ID", "7694170809"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Og_Zerathos")

# Support / Updates
SUPPORT_GRP = os.getenv("SUPPORT_GRP", "JarvisXsupport")
UPDATE_CHNL = os.getenv("UPDATE_CHNL", "botXjarvis")

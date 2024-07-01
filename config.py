# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11734178")

API_HASH = os.environ.get("API_HASH", "11e86105f12d9121b04afe06adf4d35f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7348951283:AAGa1-tUa2LhTDYhfMjBpMmxoirD38jY0os") 

FORCE_SUB = os.environ.get("FORCE_SUB", "kuku107") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "kuku")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Kuku:kuku@123@cluster0.fk02aeq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/b660e7596eed1cee3821a.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7072709969').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

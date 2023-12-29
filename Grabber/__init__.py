import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = 5830021826
sudo_users = ["2131967391", "6944102170"]
GROUP_ID = -1002062173686
TOKEN = "6877113780:AAFI8DuzehEhDnsVxGEcG2IT9CCO-xhhM9s"
mongo_url = "mongodb+srv://DevJangra:DevJangra@devdevloper.bavdfeu.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph/file/fc1212a5ca847743fb11b.jpg"]
SUPPORT_CHAT = "Alpha_Bots_Support"
UPDATE_CHAT = "Alpha_Bots_Updates"
BOT_USERNAME = "Guss_Your_Waifu_Bot"
CHARA_CHANNEL_ID = -1002062173686
api_id = 20705864
api_hash = "815880df973e10acfa73f1a12b74572b"


application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']




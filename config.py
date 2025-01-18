import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_DEFAULT_TOKEN")
DATABASE_PATH = "data/grocery.db"

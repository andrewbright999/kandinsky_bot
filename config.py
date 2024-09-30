import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

FB_SECRET = os.getenv("FB_SECRET")
SECOND_FB_SECRET = os.getenv("FB_SECRET")
FB_KEY = os.getenv("FB_KEY")
SECOND_FB_KEY = os.getenv("FB_KEY")
TG_TOKEN = os.getenv("TG_TOKEN")
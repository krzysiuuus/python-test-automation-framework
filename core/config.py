from dotenv import load_dotenv
import os

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
REQRES_BASE_URL = os.getenv("REQRES_BASE_URL")
REQRES_API_KEY = os.getenv("REQRES_API_KEY")
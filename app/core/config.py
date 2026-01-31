import os
from dotenv import load_dotenv

load_dotenv()

THEMEALDB_BASE_URL= os.getenv("THEMEALDB_BASE_URL")
TIMEOUT=int(os.getenv("TIMEOUT",10))
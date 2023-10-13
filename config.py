import os

from dotenv import load_dotenv
load_dotenv()

MONGO_URI: str = os.getenv("MONGODB_URI")
print(MONGO_URI)
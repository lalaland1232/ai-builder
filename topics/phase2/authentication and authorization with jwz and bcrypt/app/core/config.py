from dotenv import load_dotenv
load_dotenv()
import os
from dataclasses import dataclass
@dataclass
class config():
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES : int= int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    ALGORITHM: str = os.getenv("ALGORITHM")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

settings = config()
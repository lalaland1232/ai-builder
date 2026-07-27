import os
from dotenv import load_dotenv
load_dotenv()
from dataclasses import dataclass
@dataclass
class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()
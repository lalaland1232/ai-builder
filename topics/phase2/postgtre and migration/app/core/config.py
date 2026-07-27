from dotenv import load_dotenv
import os
load_dotenv()
from dataclasses import dataclass

@dataclass
class Config:
    database_url = os.getenv("DATABASE_URL")

settings = Config()
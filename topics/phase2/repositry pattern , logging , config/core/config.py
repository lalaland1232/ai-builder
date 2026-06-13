from os import getenv
from dataclasses import dataclass
@dataclass(frozen=True)
class Settings:
    print(getenv("APP_NAME"))
    App_NAME= getenv("APP_NAME")
    DEBUG=getenv("DEBUG")
    DATABASE_URL =getenv("DATABASE_URL")
    JWT_SECRET = getenv("JWT_SECRET")
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

class Settings:
    PROJECT_NAME: str = "Horus Aizat API"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

settings = Settings()

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"options": "-c time_zone='+07:00'"}
)


# print("DEBUG DATABASE_URL:", settings.DATABASE_URL)

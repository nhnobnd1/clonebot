#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5668333055:AAHSJSStdwcnvrhhqdZaObVEg_G0Nt0kD4M")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "2121142"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "73aea46b39f24bd55f967990926c32e9")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("postgresql://wzyjhhfgfoynfblbhghsfczc%40psql-mock-database-cloud:ylhshiivggwcauldbzaizwec@psql-mock-database-cloud.postgres.database.azure.com:5432/booking1673029584132dgnjnarubhaohjzd")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://postgres:hnrLHo36uM5yt4l@clone.internal:5432")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

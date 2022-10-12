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
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAgXbYAGef9hSbKjfcCYcp_eQVcqjBVP1Bcz-HeQFpOu32QwVWjBJohlQwgoaEHM4g52glA09L9gwn3bka3JOqjY1SooiO9jPrCc-IarqXZO7D7x0dfCCpCmeson3ahFIrGz0UYiV9r0mQxbd-Ut4QIY15NY3XELIWHDBlkbB54cJop69Pjc7naLDkH1VCJ1N-GrClaPAnwfJBze0p8XbaH8byfI--8F-jvgGcuyrpK7YqFxtdCDbghURSlRa6mgtj1W6EVnKSefqdSxiE7GPkgnzxPVFVH4u0hvqwoIiGU6gz2qONJLJ21cMhMbvMA_SR0lIlL_srYoDV6TBJr0U3BTlB_7wAAAAA8vrrvAA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://cnsehumnouvtlr:2d72e47d2ef2114f586fc9345a2dd04bffb2afb9583f4a481493057aa70c0d35@ec2-35-153-35-94.compute-1.amazonaws.com:5432/dd9pfob30m977q")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

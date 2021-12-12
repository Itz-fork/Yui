# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    # Your OpenAI API key
    OPENAI_KEY = os.environ.get("OPENAI_KEY")
    # Your ARQ API Key
    ARQ_API_URL = "https://thearq.tech"
    ARQ_KEY = os.environ.get("ARQ_KEY")
    # Set ON_HEROKU to False if you aren't on heroku
    ON_HEROKU = bool(os.environ.get("ON_HEROKU", False))
    HEROKU_API = os.environ.get("HEROKU_API")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    # Banned users IDs
    BANNED_USERS = set(int(usr) for usr in os.environ.get("BANNED_USERS", "12345").split())
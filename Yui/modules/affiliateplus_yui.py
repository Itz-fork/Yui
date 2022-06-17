# Copyright (c) 2021 Itz-fork

from aiohttp import ClientSession
from py_trans import Async_PyTranslator
from config import Config


class Yui_Affiliate():
    """
    AffiliatePlus Class of Yui

    Arguments:
        None

    Methods:

    """

    def __init__(self) -> None:
        self.data = {
            "age": "16",
            "birthyear": "2006",
            "birthdate": "December 15, 2006",
            "birthplace": "Earth",
            "location": "New York",
            "build": "Yui - v1.0 (Affiliate+ Engine)",
            "version": "Yui - v1.0",
            "celebrity": "Marshmello",
            "company": "Yui",
            "email": "sorry@i-dont-have-an-email.sad",
            "kindmusic": "Future bass"
        }
        self.bot_name = Config.CHAT_BOT_NAME
        self.dev_name = "Itz-fork"

    async def ask_yui(self, message, user_id):
        c_message = await self.__prepare_message(message)
        api_url = f"https://api.affiliateplus.xyz/api/chatbot?message={c_message}&botname={self.bot_name}&ownername={self.dev_name}&user={user_id}"
        for k, i in self.data.items():
            api_url += f"&{k}={i}"
        async with ClientSession() as yui_session:
            res = await yui_session.get(api_url)
            response = await res.json()
            return response["message"]

    async def __prepare_message(self, message):
        py_t = Async_PyTranslator()
        msg_origin = await py_t._detect_lang(message)
        if msg_origin != "en":
            return await py_t.translate(message, "en")
        else:
            return message

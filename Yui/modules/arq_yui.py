# Copyright (c) 2021 Itz-fork

from aiohttp import ClientSession
from Python_ARQ import ARQ, arq


class Yui_ARQ():
    """
    ARQ Class of Yui Chat Bot

    Methods:
        __close_session - Closes the aiohttp session
        ask_yui - Get response from luna chat bot
    """
    def __init__(self, api, key) -> None:
        self.session = ClientSession()
        self.arq = ARQ(api, key, self.session)
    
    async def __close_session(self, aiohtp_c):
        await aiohtp_c.close()

    async def ask_yui(self, question, user_id):
        frm_luna = await self.arq.luna(question, user_id)
        await self.__close_session(self.session)
        if frm_luna.ok:
            return frm_luna.result
        else:
            return None
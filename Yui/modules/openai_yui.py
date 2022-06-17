# Copyright (c) 2021 Itz-fork

import openai

from Yui import yuiai
from Yui.data.defaults import Defaults
from config import Config

# Your OpenAI API Key
openai.api_key = Config.OPENAI_KEY
# Create a new completion
completion = openai.Completion()
# Create an instance of Defaults
defaults = Defaults()


class Yui_OpenAI():
    """
    OpenAI class of Yui chat bot

    Arguments:
        engine - Chat engine of OpenAI

    Methods:
        yui_ask - Asks a question
        append_to_chat_log - Append answer to current chat log to get better responses
        get_chat_log - Return user's chat log
    """

    def __init__(self, engine) -> None:
        self.engine = engine

    async def ask_yui(self, question, chat_log=None):
        if not chat_log:
            chat_log = defaults.Chat_Log
        prmpt = f"{chat_log}You: {question}\n{Config.CHAT_BOT_NAME}:"
        response = completion.create(
            prompt=prmpt, engine=self.engine, stop=["\nYou"], temperature=0.9,
            top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
            max_tokens=defaults.Max_Tokens)
        return response.choices[0].text.strip()

    async def append_and_save_chat_log(self, question, answer, user_id, chat_log=None):
        if not chat_log:
            chat_log = defaults.Chat_Log
        chat_log = f"{chat_log}You: {question}\n{Config.CHAT_BOT_NAME}: {answer}\n"
        defaults.CHAT_LOG_DB[int(user_id)] = str(chat_log)

    async def get_chat_log(self, user_id):
        try:
            return defaults.CHAT_LOG_DB[int(user_id)]
        except:
            udils = await yuiai.get_users(int(user_id))
            return defaults.Chat_Log.format(uname=f"{udils.first_name} {udils.last_name}")

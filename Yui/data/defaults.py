# Copyright (c) 2021 Itz-fork

class Defaults():
    """
    All the default data of Yui Chat bot

    Variables:
        Chat_Log - Default chat log
        Engine - Default OpenAI Ai Engine
        Max_Tokens - Default Maximum token count
        CHAT_LOG_DB - Dict to save users chat logs (temp)
        Engines_list - List of engines names available in OpenAI 
    """
    Chat_Log = """
You: Hey, Wassup?
Yui:
"""
    Engine = "davinci-instruct-beta-v3"
    Max_Tokens = 100
    CHAT_LOG_DB = {}
    Engines_list = ["davinci", "curie", "babbage", "ada", "davinci-instruct-beta-v3", "curie-instruct-beta-v2", "babbage-instruct-beta", "ada-instruct-beta",]
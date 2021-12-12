# Copyright (c) 2021 Itz-fork

import re

from pyrogram import Client as yuiai, filters
from pyrogram.types import Message
from Yui.data.defaults import Defaults
from .yui_base import Yui_Base
from config import Config


# Handling Users
@yuiai.on_message(filters.private)
async def _(_, message: Message):
    if message.from_user.id in Config.BANNED_USERS:
        yui_base = Yui_Base()
        await yui_base.reply_to_user(message, await yui_base.banned_resp())
        await message.stop_propagation()
    await message.continue_propagation()     


# Bot Id
yui_bot_id = Config.BOT_TOKEN.split(":")[0]

# Chat
@yuiai.on_message(~filters.command(["engine", "help"]) & ~filters.edited & ~filters.via_bot)
async def talk_with_yui(_, message: Message):
    c_type = message.chat.type
    r_msg = message.reply_to_message
    yui_base = Yui_Base()
    if c_type == "private":
        quiz_text = message.text
    elif c_type == "supergroup" or "group":
        if message.text and re.search(r'\bYui|yui\b', message.text):
            quiz_text = message.text
        elif r_msg:
            if not r_msg.from_user:
                return
            f_usr_id = r_msg.from_user.id
            if f_usr_id == yui_bot_id:
                if message.text:
                    quiz_text = message.text
                else:
                    pass
            else:
                return
        else:
            return await message.stop_propagation()
    else:
        return await message.stop_propagation()
    # Arguments
    print("Working ;-;")
    if quiz_text:
        quiz = quiz_text.strip()
    else:
        if message.photo:
            return await yui_base.reply_to_user(message, await yui_base.image_resp())
        elif message.video or message.video_note or message.animation:
            return await yui_base.reply_to_user(message, await yui_base.vid_resp())
        elif message.document:
            return await yui_base.reply_to_user(message, await yui_base.doc_resp())
        elif message.sticker:
            return await yui_base.reply_to_user(message, await yui_base.sticker_resp())
        else:
            return await message.stop_propagation()
    usr_id = message.from_user.id
    # Get the reply from Yui
    rply = await yui_base.get_answer_from_yui(quiz, usr_id)
    await yui_base.reply_to_user(message, rply)


# Set AI Engine (For OpenAI)
@yuiai.on_message(filters.command("engine") & filters.user(Config.OWNER_ID))
async def set_yui_engine(_, message: Message):
    if len(message.command) != 2:
        engines_txt = """
**⚡️ OpenAI Engines**


**Base**

✧ `davinci` - The most capable engine and can perform any task the other models can perform and often with less instruction.
✧ `curie` - Extremely powerful, yet very fast.
✧ `babbage` - Can perform straightforward tasks like simple classification.
✧ `ada` - Usually the fastest model and can perform tasks that don’t require too much nuance.

**Instruct**

Instruct models are better at following your instructions

✧ `davinci-instruct-beta-v3`
✧ `curie-instruct-beta-v2`
✧ `babbage-instruct-beta`
✧ `ada-instruct-beta`


**👀 How to set the engines?**

To set an engine use `/engine` command followed by the engine code name you want
**Ex:**
`/engine curie-instruct-beta-v2`"""
        return await message.reply_text(engines_txt)
    else:
        yui_base = Yui_Base()
        try:
            selected_engine = message.text.split(None)[1].strip()
            if selected_engine in Defaults().Engines_list:
                await yui_base.set_ai_engine(selected_engine)
                await message.reply(f"**Successfully Changed OpenAI Engine** \n\n**New Engine:** `{selected_engine}`")
            else:
                await message.reply("**Invalid Engine Selected!**")
        except:
            await message.reply(await yui_base.emergency_pick())


# Ban users
@yuiai.on_message(filters.command("ban") & filters.user(Config.OWNER_ID))
async def ban_usr_fbot(_, message: Message):
    if len(message.command) != 2:
        return await message.reply("**Give a user id to ban!**")
    else:
        yui_base = Yui_Base()
        try:
            usr_id = message.text.split(None)[1].strip()
            if Config.ON_HEROKU:
                await yui_base.ban_usr(usr_id)
                await message.reply(f"**Successfully Banned That User** \n\n**User ID:** `{usr_id}`")
            else:
                await message.reply("**Only available for Heroku!**")
        except:
            await message.reply(await yui_base.emergency_pick())
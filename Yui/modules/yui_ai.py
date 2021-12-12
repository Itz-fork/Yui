# Copyright (c) 2021 Itz-fork

from pyrogram import Client as yuiai, filters
from pyrogram.types import Message
from .yui_base import Yui_Base
from Yui.data.defaults import Defaults
from config import Config


# Chat
@yuiai.on_message(~filters.command(["engine", "help"]) & ~filters.edited & ~filters.via_bot)
async def talk_with_yui(_, message: Message):
    c_type = message.chat.type
    yui_base = Yui_Base()
    if c_type == "private":
        print(f"Private: {message.text}")
        quiz_text = message.text
    elif c_type == "supergroup" or "group":
        # Was going to use regex but this is still ok tho
        if "Yui" or "yui" in message.text:
            print(f"Group: {message.text}")
            quiz_text = message.text
        else:
            await message.stop_propagation()
            return
    else:
        await message.stop_propagation()
        return
    # Arguments
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
            await message.stop_propagation()
            return
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

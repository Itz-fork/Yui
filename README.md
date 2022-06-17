# Yui

***Yui, is a simple telegram chat bot made using OpenAI, AFFILIATE+ and Luna Chat bot***

----

## Deployment 👀

Deploying is easy 🤫! You can deploy this bot in Heroku or in a VPS ♥️! **Star 🌟 Fork 🍴 and Deploy**

#### With Heroku

<a href="https://www.heroku.com/deploy?template=https://github.com/Itz-fork/Yui">
  <img src="https://www.herokucdn.com/deploy/button.svg">
</a>

#### Self-Hosting

```bash
git clone https://github.com/Itz-fork/Yui.git
cd Yui
pip3 install -r requirements.txt
```

**Edit "config.py" with your own values**

```bash
python3 -m Yui
```


## Configs 🗒️

- `APP_ID` - Your APP ID. Get it from [my.telegram.org](my.telegram.org)
- `API_HASH` - Your API_HASH. Get it from [my.telegram.org](my.telegram.org)
- `BOT_TOKEN` - Bot Token of Your Telegram Bot. Get it from [@BotFather](https://t.me/BotFather)
- `OWNER_ID` - Your Telegram Account ID. Get it from [@MissRose_bot](https://t.me/MissRose_bot) (Start the bot and send <samp>/info</samp> command)
- `CHAT_BOT_NAME` - Custom name for your chatbot. (Default to `Yui`)
- `OPENAI_KEY` - Your own [OpenAI](https://openai.com/) API Key
  - Go to [OpenAI Sign Up Page](https://beta.openai.com/signup) and create your OpenAI Account
  - Then go to [API Keys Section](https://beta.openai.com/account/api-keys)
  - From there you can copy your OpenAI API Key
- `ARQ_KEY` - Your ARQ API Key. Get it from [@ARQRobot](https://t.me/ARQRobot)
- `DEFAULT_CHATBOT` - The Default chatbot you want to use after OpenAI. (`affiliateplus` or `luna`)
- `MAX_TOKENS` - The maximum number of tokens to generate in the completion

**For Heroku Users,**

- `ON_HEROKU` - Set this var to `True`
- `HEROKU_APP_NAME` - Your Heroku app name
- `HEROKU_API` - Your Heroku API
  - Go to [account dashboard](https://dashboard.heroku.com/account)
  - Scroll down and find the "API Key" section and click on Reveal button to get your API Key


### Note ⚠️

If you want to increase the response length limit change [Max Response Length Limit Value](https://github.com/Itz-fork/Yui/blob/ef431bb67f5c51ee3d5a634d91a2b0f740192d36/Yui/data/defaults.py#L19) to whatever you want (Value must be a integer). Also increasing this can spend your OpenAI credits quickly

## Support 🍪

<a href="https://t.me/NexaBotsUpdates">
  <img src="https://img.shields.io/badge/Updates_Channel-0a0a0a?style=for-the-badge&logo=telegram&logoColor=white">
</a>
<a href="https://t.me/Nexa_bots">
  <img src="https://img.shields.io/badge/Support_Group-0a0a0a?style=for-the-badge&logo=telegram&logoColor=white">
</a>

</br>


## License & Copyright 👮

```
Copyright (c) 2021 Itz-fork

This Yui repository is licensed under GPLv3 License (https://github.com/Itz-fork/Yui/blob/master/LICENSE)
Copying or Modifying Any Part of the code without permission is strictly prohibited
```

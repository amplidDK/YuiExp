## YuiExp. TgBot to convert voice message to text


### Local run:
- #### Clone project
- #### Install Poetry
- #### install ffmpeg
- #### Create config.py
- #### Save your bot token to BOT_TOKEN variable(if haven't yet - create one with BotFather)
- #### Run terminal command `poetry install`
- #### Run program and send voice to your bot


### Friendly reminder:
#### This bot using is `whisper-1` OPENAI model. To be able to use this model, you need to get token from OPENAI. You should also to add this token to `config.py` with `OPENAI_TOKEN` name.

#### If it isn't possible - you may change recognizer from `recognize_whisper_api` to `recognize_google_cloud`. Quality will be worse, but it's easier to run.
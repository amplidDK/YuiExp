from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.types import File, Message

import paths
from config import BOT_TOKEN
from utils.ogg_worker import remove_ogg
from utils.voice_msg_converter import send_text_from_voice

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()


async def handle_file(file: File, file_name: str, path: str):
    Path(f'{path}').mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f'{path}/{file_name}')


@dp.message(lambda message: message.voice)
async def voice_message_handler(message: Message):
    await handle_file(file=await bot.get_file(message.voice.file_id), file_name=f'{message.voice.file_id}.ogg',
                      path=paths.VOICES_DIR)

    await message.reply(text=send_text_from_voice(message.voice.file_id))
    remove_ogg(f'{paths.VOICES_DIR}/{message.voice.file_id}.ogg')

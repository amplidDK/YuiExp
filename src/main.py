import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.types import File, Message

import config
from utils.voice_msg_converter import send_text_from_voice

bot: Bot = Bot(config.BOT_TOKEN)
dp: Dispatcher = Dispatcher()


async def handle_voice_file(file: File, file_name: str, path: str):
    Path(f'{path}').mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f'{path}/{file_name}')

def remove_ogg(file_path):
    os.remove(file_path)
@dp.message(lambda message: message.voice)
async def voice_message_handler(message: Message):
    file_id = message.voice.file_id
    voice = await bot.get_file(message.voice.file_id)
    path = f'{config.ROOT_DIR}/src'

    await handle_voice_file(file=voice, file_name=f'{file_id}.ogg', path=path)

    await message.reply(text=send_text_from_voice())
    remove_ogg(f'{file_id}.ogg')


if __name__ == '__main__':
    dp.run_polling(bot)

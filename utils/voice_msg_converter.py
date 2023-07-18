import os

import speech_recognition as sr
from pydub.audio_segment import AudioSegment

import paths
from config import OPENAI_TOKEN
from utils.ogg_worker import get_ogg_file

r: sr = sr.Recognizer()


def convert_ogg_to_flac(file_id):
    if not os.path.exists(paths.AUDIOS_DIR):
        os.mkdir(paths.AUDIOS_DIR)
    src = AudioSegment.from_ogg(get_ogg_file())
    src.export(f'{paths.AUDIOS_DIR}/{file_id}.FLAC', format='FLAC')

    return sr.AudioFile(f'{paths.AUDIOS_DIR}/{file_id}.FLAC')


def extract_text(audio_file):
    with convert_ogg_to_flac(audio_file) as source:
        audio = r.record(source)

    text = r.recognize_whisper_api(audio_data=audio, model='whisper-1', api_key=OPENAI_TOKEN)
    os.remove(f'{paths.AUDIOS_DIR}/{audio_file}.FLAC')

    return text

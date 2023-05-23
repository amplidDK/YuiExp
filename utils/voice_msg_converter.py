import os
import speech_recognition as sr
from pydub.audio_segment import AudioSegment

import paths
from utils.ogg_worker import get_ogg_file


# TODO refactor to few functions
def send_text_from_voice(file_id):
    if not os.path.exists(paths.AUDIOS_DIR):
        os.mkdir(paths.AUDIOS_DIR)
    src = AudioSegment.from_ogg(get_ogg_file())
    src.export(f'{paths.AUDIOS_DIR}/{file_id}.wav', format='wav')

    r = sr.Recognizer()
    audio_file = sr.AudioFile(f'{paths.AUDIOS_DIR}/{file_id}.wav')

    with audio_file as source:
        audio = r.record(source)

    text = r.recognize_google(audio, language='ru-RU')
    os.remove(f'{paths.AUDIOS_DIR}/{file_id}.wav')

    return text



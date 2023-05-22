import os
from pathlib import Path

import config
from pydub.audio_segment import AudioSegment
import speech_recognition as sr
def get_pdf_file():
    pth = Path().cwd()
    pdf_files = list(pth.glob('*.ogg'))
    return pdf_files[-1]

def send_text_from_voice():
    src = AudioSegment.from_ogg(get_pdf_file())
    src.export('test.wav', format='wav')

    r = sr.Recognizer()
    audio_file = sr.AudioFile(f'{config.ROOT_DIR}/src/test.wav')

    with audio_file as source:
        audio = r.record(source)


    text = r.recognize_google(audio, language='ru-RU')
    os.remove(f'{config.ROOT_DIR}/src/test.wav')

    return text

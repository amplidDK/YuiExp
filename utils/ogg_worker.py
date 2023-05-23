from pathlib import Path
import os
import paths


def get_ogg_file():
    path = Path(paths.VOICES_DIR)
    ogg_files = list(path.glob('*.ogg'))
    return ogg_files[-1]


def remove_ogg(file_path):
    os.remove(file_path)

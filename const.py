import sys
from utils import *
from os import listdir
from os.path import isfile, join, abspath

VERSION = '1.0.0'

MAX_LINE_LENGTH = 35
MAX_LINES = 7

TXT_SPACE = "゜"
TXT_FILL = "█"

GITHUB = "https://github.com/realooffyy/Minecraft-ASCII-Text-Generator"
GITHUB_HOWTO = "https://github.com/realooffyy/Minecraft-ASCII-Text-Generator?tab=readme-ov-file#how-to-use"

def resource_path(relative_path): # https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath(".")

    return join(base_path, relative_path)

CHARDIR = resource_path("./characters") # fix for pyinstaller
#DIRECTORY = pathlib.Path().resolve()
#CHARDIR = os.path.join(DIRECTORY, "characters")

# creates an array with all existing character files
CHARS = [f[:-5] for f in listdir(CHARDIR) if isfile(join(CHARDIR, f)) and f.endswith(".char")]
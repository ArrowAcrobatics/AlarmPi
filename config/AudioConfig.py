from os import listdir
from os.path import isfile, join
from pathlib import Path

class AudioConfig:
    def __init__(self, rootdirpath: Path):
        self.SOUNDS_DIRECTORY = rootdirpath/"sounds"
        self.SOUND_FILE_EXT = ".wav"
        self.auto_set_audio_device = True

        self.SPEECH_VOLUME = 80  # percent
        self.ESPEAK_SPEECH_VOICE = "en+m3"  # en+f4 # see http://espeak.sourceforge.net/languages.html
        self.ESPEAK_SPEECH_SPEED = 150
        # YAKITTOME_SPEECH_VOICE = "Audrey" # see https://www.yakitome.com/documentation/tts_voices
        # YAKITTOME_SPEECH_SPEED = 5
        # YAKITTOME_API_KEY = "" #"utvWYeYhzFJtl1ausX690QY"

    def Sounds(self):
        """ Returns all the filenames (sound IDs for this program) of the sounds in the /sounds folder.
    	While not techinally returning an array of constants, represents a series of constants.
    	Adapted from http://stackoverflow.com/a/3207973/3155372 """
        return [f[:f.rindex(".")] for f in listdir(self.SOUNDS_DIRECTORY) if
                isfile(join(self.SOUNDS_DIRECTORY, f))]  # Communications




# AlarmUtility.py
#
# A place for shared utiliy methods, many of which are related to 
# the constants in AlarmConstants.py
#
# Mckenna Cisler
# mckennacisler@gmail.com
# 7.4.2016

import json
import urllib
import urllib.request


def getPrettyName(setting):
    setting = setting.replace("_", " ")

    result = ""
    for word in setting.split(" "):
        result += word[0].upper() + word[1:] + " "
    return result[:len(result) - 1]  # remove space


def SettingsAsList(cls, sortkey=None):
    """ Returns a list representing the values of the constants in the class `cls`."""
    settingArr = []
    for setting in cls.__dict__.keys():
        if (not setting.startswith("__")):
            settingArr.append(cls.__dict__[setting])
    # sort return for consistency
    return sorted(settingArr, key=sortkey)

def getJSON(url, values):
    params = urllib.urlencode(values)
    req = urllib.request.Request(url, params)
    response = urllib.request.urlopen(req)
    return json.loads(response.read())


# def speak(string):
#     log("SPEAKING: " + string)
#
#     setVolume(SPEECH_VOLUME)
#
#     if (YAKITTOME_API_KEY != ""):
#         # send request to get audio from YAKItToMe
#         # resources:
#         # https://www.yakitome.com/documentation/tts_api#markmin_tts
#         # https://docs.python.org/2/library/urllib.html#urllib.urlretrieve
#
#         # get the book id, which allows us to get the audio file
#         valuesTTS = dict(
#             api_key=YAKITTOME_API_KEY,
#             voice=YAKITTOME_SPEECH_VOICE,
#             speed=YAKITTOME_SPEECH_SPEED,
#             text=string)
#         jsonTTSResponse = getJSON("http://www.yakitome.com/api/rest/tts", valuesTTS)
#         bookID = jsonTTSResponse['book_id']
#
#         # get the url of the relevant audio file
#         valuesAudio = dict(
#             api_key=YAKITTOME_API_KEY,
#             book_id=bookID,
#             format="ogg")
#         jsonAudioResponse = getJSON("http://www.yakitome.com/api/rest/audio", valuesAudio)
#         fileURL = jsonAudioResponse["audios"][0]
#
#         # download file and play it
#         location = u"/tmp/" + fileURL[fileURL.rindex("/"):]
#         log("Downloading + playing file " + location)
#         sub.call(["wget", "--output-document=%s" % location, fileURL])
#         sub.call(["play", location, "&"])
#
#     else:
#         location = "/tmp/" + str(time.time()) + ".wav"
#         sub.call(["pico2wave", "-l=en-US", "-w=%s" % location, string])
#         sub.call(["aplay", location])
#
#         """
#         # call espeak to get audio data
#         espeak_ps = sub.Popen(["espeak", '"' + string + '"',
#                                "--stdout",
#                                "-s", str(ESPEAK_SPEECH_SPEED),
#                                "-v", ESPEAK_SPEECH_VOICE],
#                               stdout=sub.PIPE)
#
#         # then pipe it to aplay to fix bitrate issue
#         sub.call(["aplay"], stdin=espeak_ps.stdout)
#         """

if __name__ == "__main__":
    speak("Hello, world")

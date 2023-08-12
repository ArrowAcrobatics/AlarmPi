# AlarmActivator.py
#
# Resposible for activating and managing
# the sound aspects of the alarm when it is going off.
#
# Mckenna Cisler
# mckennacisler@gmail.com
# 1.13.2019
import subprocess

from config.AlarmConstants import DailySetting, REPEAT_NUM, AlarmType
from config.Config import GlobalConfig

import asyncio


class AlarmActivator:
    """ TODO(Arend): implement VLC backend"""

    def __init__(self, day):
        self.alarmType = GlobalConfig.alarm.getDailySetting(day, DailySetting.ALARM_TYPE)
        self.subType = GlobalConfig.alarm.getDailySetting(day, DailySetting.ALARM_SUBTYPE)

        self._soundProcess = None

    async def activate(self):
        if self._soundProcess is not None:
            self._soundProcess.kill()

        startplaylistcmd = f"vlc {GlobalConfig.audio.SOUNDS_DIRECTORY}/Neon.wav"
        print(startplaylistcmd)
        self._soundProcess = await asyncio.create_subprocess_shell(
            startplaylistcmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

    def _activateSound(self, sound):
        self._soundProcess = sub.Popen(
            ["play", GlobalConfig.audio.SOUNDS_DIRECTORY + sound + SOUND_FILE_EXT, "repeat", str(REPEAT_NUM)])
        # TODO: Check if successful

    async def deactivate(self):
        if self._soundProcess != None:
            self._soundProcess.kill()


if __name__ == "__main__":
    import time
    async def main():
        activator = AlarmActivator('thurs')
        await activator.activate()
        await asyncio.sleep(5)
        await activator.deactivate()

    asyncio.get_event_loop().run_until_complete(main())


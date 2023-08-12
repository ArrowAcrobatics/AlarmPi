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
    def __init__(self, quiet=True, random=False):
        self._soundProcess = None
        self.quietFlag = "--quiet" if quiet else ""
        self.modeFlag = "--random" if random else "--loop"

        self.commands = "play stop pause prev next".split()
        self.setters = "volup voldown goto".split()

        self.playlist = "Neon.wav Portal.wav Platinum.wav".split()

    async def activate(self):
        if self._soundProcess is not None:
            self._soundProcess.kill()

        startplaylistcmd = " ".join(
            filter(None, ["vlc", self.quietFlag] + [str(GlobalConfig.audio.SOUNDS_DIRECTORY / song) for song in
                                                    self.playlist]))
        print(startplaylistcmd)
        self._soundProcess = await asyncio.create_subprocess_shell(
            startplaylistcmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        self.volume(GlobalConfig.audio.ALARM_VOLUME)

    async def deactivate(self):
        if self._soundProcess != None:
            await self.write_vlc_command("quit")

    ### vlc commands
    async def pause(self):
        if self._soundProcess != None:
            await self.write_vlc_command("pause")

    async def play(self):
        if self._soundProcess != None:
            await self.write_vlc_command("play")

    async def next(self):
        if self._soundProcess != None:
            await self.write_vlc_command("next")

    async def prev(self):
        if self._soundProcess != None:
            await self.write_vlc_command("prev")

    async def volup(self, steps=1):
        if self._soundProcess != None:
            await self.write_vlc_command(f"volup {steps}")

    async def voldown(self, steps=1):
        if self._soundProcess != None:
            await self.write_vlc_command(f"voldown {steps}")

    async def volume(self, value=80):
        if self._soundProcess != None:
            await self.write_vlc_command(f"volume {value}")

    async def goto(self, index=1):
        if self._soundProcess != None:
            await self.write_vlc_command(f"goto {index}")

    async def write_vlc_command(self, commandstr):
        """ Boilerplate for vlc commands. """
        if self._soundProcess is None:
            print("WARNING _soundProcess is None")
            return

        print(f"writing: {commandstr} to : {self._soundProcess.stdin}")
        commandstr += "\n"
        self._soundProcess.stdin.write(commandstr.encode())
        await self._soundProcess.stdin.drain()

    # IO related stuff
    async def read_std_pipe(self, name, pipe):
        """ Read data and print from given pipe (StreamReader). """
        print(f'read from pipe: {name}')
        while True:
            buf = await pipe.read(10)
            if not buf:
                break

            print(f'{name}: {buf}')

    async def run_io(self):
        """ Runs all the pipe co-routines at onces. TODO: Should be reinitialized after killing the _soundProcess. """
        print("running io now")
        try:
            await asyncio.gather(self.read_std_pipe("stdout", self._soundProcess.stdout),
                                 self.read_std_pipe("stderr", self._soundProcess.stdout))
        except asyncio.CancelledError as e:
            print("io cancelled running: ", e)


if __name__ == "__main__":
    async def main():
        activator = AlarmActivator(random=True)
        await activator.activate()
        # asyncio.create_task(activator.run_io())  # if you want to read the garbage from vlc
        await asyncio.sleep(5)
        await activator.write_vlc_command("pause")
        await asyncio.sleep(5)
        await activator.write_vlc_command("play")
        await asyncio.sleep(5)
        await activator.deactivate()


    asyncio.get_event_loop().run_until_complete(main())

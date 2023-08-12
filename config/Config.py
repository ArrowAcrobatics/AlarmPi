import os
from pathlib import Path

from config.AlarmConfig import AlarmConfig
from config.AudioConfig import AudioConfig
from config.ServerConfig import ServerConfig
import logging

class Config:
    def __init__(self):
        # "/home/pi/sync/Projects/Coding/project/RPi/AlarmPi/"
        self.ROOT_DIRECTORY = Path().home() / "alarmpi"

        self.CONFIG_FILE = self.ROOT_DIRECTORY / "alarm-config.json"
        self.LOGFILE = self.ROOT_DIRECTORY/"alarmpi.log"

        self.audio = AudioConfig(self.ROOT_DIRECTORY)
        self.server = ServerConfig(self.ROOT_DIRECTORY)
        self.alarm = AlarmConfig(self.ROOT_DIRECTORY / "alarm-config.json")

        self.debug = False


GlobalConfig = Config()

logging.basicConfig(
    level=logging.DEBUG,
    filename=GlobalConfig.LOGFILE,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

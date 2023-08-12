# AlarmConstants.py
#
# This file defines constants
#
# Mckenna Cisler
# mckennacisler@gmail.com
# 1.13.2019

# Global Constants

# TODO(Arend): move to AlarmConfig
REPEAT_NUM = 50  # number of times to loop sounds
# TODO(Arend): move to AlarmConfig
CYCLE_ALIGNED_EARLIEST_SET_TOMMOROW = 8  # hour (24hr) of the day to switch to setting cycle-aligned alarm for the next day



class AlarmType:
    SOUND = "sound"
    PANDORA = "pandora"


# NOTES:
# All daily settings are designed to be set and changed globally as well (via iteration)
# All duration values are in seconds
# See AlarmConfig._generateNewConfig() for default values (they're only used there)

class DailySetting:
    ALARM_TYPE = "type"
    ALARM_SUBTYPE = "subtype"
    TIME_TO_SLEEP = "time_to_sleep"  # seconds
    DESIRED_SLEEP_TIME = "desired_sleep_time"  # seconds; desired time to sleep for using cycle-aligned alarm
    MAX_OVERSLEEP = "max_oversleep"  # seconds; max time for a cycle-aligned alarm to go over the desired wakeup
    # (O means always round down; 90 (maximum) means always round up)


class GlobalSetting:
    ALARM_VOLUME = "alarm_volume"  # value is in range(100)
    SNOOZE_TIME = "snooze_time"  # value is time in seconds to snooze for
    ACTIVATION_TIMEOUT = "activation_timeout"  # value is time in seconds to wait before forcing alarm shutdown


def SettingsAsList(cls):
    """ Returns a list representing the values of the constants in the class `cls`."""
    settingArr = []
    for setting in cls.__dict__.keys():
        if (not setting.startswith("__")):
            settingArr.append(cls.__dict__[setting])
    # sort return for consistency
    return sorted(settingArr)


def GlobalSettings():
    """ Returns a list representing the values of the constants in the class GlobalSettings."""
    return SettingsAsList(GlobalSetting)


def DailySettings():
    """ Returns a list representing the values of the constants in the class DailySettings."""
    return SettingsAsList(DailySetting)

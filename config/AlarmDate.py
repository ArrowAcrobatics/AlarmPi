from backend.AlarmUtility import SettingsAsList


# Constant "Enum" Classes
class Day:
    MON = "mon"
    TUES = "tues"
    WED = "wed"
    THURS = "thurs"
    FRI = "fri"
    SAT = "sat"
    SUN = "sun"


def getDayFromNum(dayNum):
    if (dayNum == 0): return Day.MON
    if (dayNum == 1): return Day.TUES
    if (dayNum == 2): return Day.WED
    if (dayNum == 3): return Day.THURS
    if (dayNum == 4): return Day.FRI
    if (dayNum == 5): return Day.SAT
    if (dayNum == 6): return Day.SUN


def getNumFromDay(day):
    if (day == Day.MON):    return 0
    if (day == Day.TUES):    return 1
    if (day == Day.WED):    return 2
    if (day == Day.THURS):    return 3
    if (day == Day.FRI):    return 4
    if (day == Day.SAT):    return 5
    if (day == Day.SUN):    return 6


def getFullDayName(day):
    if (day == Day.MON):    return "Monday"
    if (day == Day.TUES):    return "Tuesday"
    if (day == Day.WED):    return "Wednesday"
    if (day == Day.THURS):    return "Thursday"
    if (day == Day.FRI):    return "Friday"
    if (day == Day.SAT):    return "Saturday"
    if (day == Day.SUN):    return "Sunday"


def Days():
    """ Returns a list representing the values of the constants in the class Days."""
    return SettingsAsList(Days, sortkey=getNumFromDay)
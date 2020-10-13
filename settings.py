import json

with open('settings.json') as f:
    settings = json.load(f)
    """
    Imports the Json file as settings
    """


def height():
    """
    Will take the display Height value from a Json file (for ease of use)
    :return:
    """
    displayHeight = settings["displayHeight"]
    return displayHeight


def width():
    """
    Will take the display Width value from a Json file (for ease of use)
    :return:
    """
    displayWidth = settings["displayWidth"]
    return displayWidth


def FPS():
    """
    Will take the display's FrameRate value from a Json file (for ease of use)
    :return:
    """
    frameRate = settings["frameRate"]
    return frameRate


def screen():
    """
    Will take the display number (in case you have multiple screens) value from a Json file (for ease of use)
    :return:
    """
    displayNumber = settings["displayNumber"]
    return displayNumber

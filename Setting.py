import json

with open("settings.json", "r") as r:
    data = json.load(r)


def resolution():
    return [data["displayResWidth"], data["displayresHeight"]]


def keyboardInput(direction):
    if direction == "UP":
        return data["movementJump"]
    if direction == "LEFT":
        return data["movementStrafeLeft"]
    if direction == "RIGHT":
        return data["movementStrafeRight"]
    if direction == "DOWN":
        return data["movementDown"]


def Volume(type):
    if type == "Music":
        return round(data["MusicVolume"])
    if type == "MusicMute":
        return data["MusicVolumeMute"]
    if type == "Sounds":
        return round(data["SoundsVolume"])
    if type == "SoundsMute" :
        return data["SoundsVolumeMute"]

print("Settings : " "\nMove UP : ", keyboardInput("UP"), "\nMove Left : ", keyboardInput("LEFT"), "\nMove Right : ", keyboardInput("RIGHT"), "\nMove Downw : ", keyboardInput("DOWN"), "\nResolution : ",resolution(), "\nMusic Volume : ", Volume("Music"), " %\nSound Volume : ", Volume("Sounds"), "%\nMusic Muted : ", Volume("MusicMute"), "\nSounds Muted : ", Volume("SoundsMute"))


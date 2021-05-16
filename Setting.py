import json
import pygame

# Dumps content from json file to a list
with open("settings.json", "r") as r:
    data = json.load(r)


# return resolution in a list format
def resolution():
    return [data["displayResWidth"], data["displayresHeight"]]


# Syntax simplification for resolution
ScreenWidth = resolution()[0]
ScreenHeight = resolution()[1]

# Kebinds dispatcher (Using AZERTY layout)
dispatcher = {"K_a": pygame.K_q, "K_b": pygame.K_b, "K_c": pygame.K_c, "K_d": pygame.K_d, "K_e": pygame.K_e,
              "K_f": pygame.K_f, "K_g": pygame.K_g, "K_h": pygame.K_h, "K_i": pygame.K_i, "K_j": pygame.K_j,
              "K_k": pygame.K_k, "K_l": pygame.K_l, "K_m": pygame.K_SEMICOLON, "K_n": pygame.K_n, "K_o": pygame.K_o,
              "K_p": pygame.K_p, "K_q": pygame.K_a, "K_r": pygame.K_r, "K_s": pygame.K_s, "K_t": pygame.K_t,
              "K_u": pygame.K_u, "K_v": pygame.K_v, "K_w": pygame.K_z, "K_x": pygame.K_x, "K_y": pygame.K_y,
              "K_z": pygame.K_w, "K_SPACE": pygame.K_SPACE, "K_LEFT": pygame.K_LEFT, "K_UP": pygame.K_UP,
              "K_DOWN": pygame.K_DOWN, "K_RIGHT": pygame.K_RIGHT, "K_LSHIFT": pygame.K_LSHIFT,
              "K_LCTRL": pygame.K_LCTRL}


# Left movement function
def moveLeft():
    Left = data["movementStrafeLeft"]
    return dispatcher[Left]


# Right movement function
def moveRight():
    Right = data["movementStrafeRight"]
    return dispatcher[Right]


# Down movement function
def moveDown():
    Up = data["movementDown"]
    return dispatcher[Up]


# Jump movement function
def moveUp():
    Down = data["movementJump"]
    return dispatcher[Down]


# Sound settings handler
def Volume(arg):
    if arg == "Music":
        return int(round(data["MusicVolume"]))
    if arg == "MusicMute":
        return data["MusicVolumeMute"]
    if arg == "Sounds":
        return int(round(data["SoundsVolume"]))
    if arg == "SoundsMute":
        return data["SoundsVolumeMute"]


# Prints all settings (for debugging)
print("Settings : " "\nMove UP : ", data["movementJump"], "\nMove Left : ", data["movementStrafeLeft"],
      "\nMove Right : ", data["movementStrafeRight"], "\nMove Down : ", data["movementDown"], "\nResolution : ",
      resolution(), "\nMusic Volume : ", Volume("Music"), "%\nSound Volume : ", Volume("Sounds"), "%\nMusic Muted : ",
      Volume("MusicMute"), "\nSounds Muted : ", Volume("SoundsMute"))

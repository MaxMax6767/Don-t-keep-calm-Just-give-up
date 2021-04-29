import json
import pygame

with open("settings.json", "r") as r:
    data = json.load(r)


def resolution():
    return [data["displayResWidth"], data["displayresHeight"]]


ScreenWidth = resolution()[0]
ScreenHeight = resolution()[1]

dispatcher = {"K_a": pygame.K_q, "K_b": pygame.K_b, "K_c": pygame.K_c, "K_d": pygame.K_d, "K_e": pygame.K_e,
              "K_f": pygame.K_f, "K_g": pygame.K_g, "K_h": pygame.K_h, "K_i": pygame.K_i, "K_j": pygame.K_j,
              "K_k": pygame.K_k, "K_l": pygame.K_l, "K_m": pygame.K_SEMICOLON, "K_n": pygame.K_n, "K_o": pygame.K_o,
              "K_p": pygame.K_p, "K_q": pygame.K_a, "K_r": pygame.K_r, "K_s": pygame.K_s, "K_t": pygame.K_t,
              "K_u": pygame.K_u, "K_v": pygame.K_v, "K_w": pygame.K_z, "K_x": pygame.K_x, "K_y": pygame.K_y,
              "K_z": pygame.K_w, "K_SPACE": pygame.K_SPACE, "K_LEFT": pygame.K_LEFT, "K_UP": pygame.K_UP,
              "K_DOWN": pygame.K_DOWN, "K_RIGHT": pygame.K_RIGHT, "K_LSHIFT": pygame.K_LSHIFT,
              "K_LCTRL": pygame.K_LCTRL}


def moveLeft():
    Left = data["movementStrafeLeft"]
    return dispatcher[Left]


def moveRight():
    Right = data["movementStrafeRight"]
    return dispatcher[Right]


def moveDown():
    Up = data["movementDown"]
    return dispatcher[Up]


def moveUp():
    Down = data["movementJump"]
    return dispatcher[Down]


def Volume(type):
    if type == "Music":
        return int(round(data["MusicVolume"]))
    if type == "MusicMute":
        return data["MusicVolumeMute"]
    if type == "Sounds":
        return int(round(data["SoundsVolume"]))
    if type == "SoundsMute":
        return data["SoundsVolumeMute"]


print("Settings : " "\nMove UP : ", data["movementJump"], "\nMove Left : ", data["movementStrafeLeft"],
      "\nMove Right : ", data["movementStrafeRight"], "\nMove Down : ", data["movementDown"], "\nResolution : ",
      resolution(), "\nMusic Volume : ", Volume("Music"), "%\nSound Volume : ", Volume("Sounds"), "%\nMusic Muted : ",
      Volume("MusicMute"), "\nSounds Muted : ", Volume("SoundsMute"))

print(resolution()[0])

print(ScreenHeight + (round(ScreenHeight / 720 * 20 - round(ScreenHeight / 720 * 30))))

import pygame
from Setting import Volume
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.mixer.pre_init(44100, -16, 2, 2048)  # Initialises the sound for pygame
pygame.init()  # Initialises pygame itself


def music(arg):
    """
    If the music is not muted by the json file, play music at the volume given by the json file and loops it while the aragument is not "Stop"
    """
    if not Volume("MusicMute"):
        pygame.mixer.music.load(resource_path("musique/music.mp3"))
        pygame.mixer.music.set_volume(Volume("Music")/100)
        if arg == "play":
            pygame.mixer.music.play(loops=-1)
        if arg == "stop":
            pygame.mixer.music.stop()

def door(arg):
    """
    If the sounds are not muted by the json file, play door sound at the volume given by the json file while the aragument is not "Stop"
    """
    if not Volume("SoundsMute"):
        pygame.mixer.music.load(resource_path("musique/door.mp3"))
        pygame.mixer.music.set_volume(Volume("Sounds")/100)
        if arg == "play":
            pygame.mixer.music.play()
        if arg == "stop":
            pygame.mixer.music.stop()

def death(arg):
    """
    If the sounds are not muted by the json file, play death sound at the volume given by the json file while the aragument is not "Stop"
    """
    if not Volume("SoundsMute"):
        pygame.mixer.music.load(resource_path("musique/Dead.mp3"))
        pygame.mixer.music.set_volume(Volume("Sounds")/100)
        if arg == "play":
            pygame.mixer.music.play()
        if arg == "stop":
            pygame.mixer.music.stop()

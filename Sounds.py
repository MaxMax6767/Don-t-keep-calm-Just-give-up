import pygame
from Setting import Volume

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

def music(arg):
    if not Volume("MusicMute"):
        pygame.mixer.music.load("musique/music.mp3")
        pygame.mixer.music.set_volume(Volume("Music")/100)
        if arg == "play":
            pygame.mixer.music.play(loops=-1)
        if arg == "stop":
            pygame.mixer.music.stop()

def door(arg):
    if not Volume("SoundsMute"):
        pygame.mixer.music.load("musique/door.mp3")
        pygame.mixer.music.set_volume(Volume("Sounds")/100)
        if arg == "play":
            pygame.mixer.music.play()
        if arg == "stop":
            pygame.mixer.music.stop()

def death(arg):
    if not Volume("SoundsMute"):
        pygame.mixer.music.load("musique/Dead.mp3")
        pygame.mixer.music.set_volume(Volume("Sounds")/100)
        if arg == "play":
            pygame.mixer.music.play()
        if arg == "stop":
            pygame.mixer.music.stop()

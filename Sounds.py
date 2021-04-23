import pygame
import os
os.getcwd()

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

def music(arg):
    pygame.mixer.music.load("musique/music.mp3")
    pygame.mixer.music.set_volume(0.8)
    if arg == "play":
        pygame.mixer.music.play(loops=-1)
    if arg == "stop":
        pygame.mixer.music.stop()

def door(arg):
    pygame.mixer.music.load("musique/door.mp3")
    pygame.mixer.music.set_volume(0.8)
    if arg == "play":
        pygame.mixer.music.play()
    if arg == "stop":
        pygame.mixer.music.stop()

def death(arg):
    pygame.mixer.music.load("musique/Dead.mp3")
    pygame.mixer.music.set_volume(0.8)
    if arg == "play":
        pygame.mixer.music.play()
    if arg == "stop":
        pygame.mixer.music.stop()

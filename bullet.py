import pygame
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# This object is not used just yet, it will come in future updates

# Class for the gun's bullets
class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # Image and coordinates
        self.image = pygame.image.load(resource_path('images/bullet.jpg'))
        self.image = pygame.transform.scale(self.image, (10, 5))
        self.rect = self.image.get_rect()
        self.rect.x = 130
        self.rect.y = 635
        # player loose life
        self.life = -1

    def move(self):
        """Gives motion to the bullets"""
        self.rect.x += 20

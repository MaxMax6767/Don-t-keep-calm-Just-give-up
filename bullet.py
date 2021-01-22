import pygame


# Class for the gun's bullets
class Bullet(pygame.sprite.Sprite):

    def __init__(self, gun):
        super().__init__()
        self.image = pygame.image.load('images/bullet.jpg')
        self.image = pygame.transform.scale(self.image, (10, 5))
        self.rect = self.image.get_rect()
        self.rect.x = 130
        self.rect.y = 635
        self.life = -2

    def move(self):
        """Gives motion to the bullets"""
        self.rect.x += 20

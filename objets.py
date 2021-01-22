import pygame
from bullet import Bullet


# Class for walls
class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, long, height):
        super().__init__()
        # Loads the image and resizes it
        self.image = pygame.image.load('images/wall.jpg')
        self.image = pygame.transform.scale(self.image, (long, height))
        # Handles the screen coordinates
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_bottom = pygame.Rect(x + 5, y - height, long - 15, 1)
        self.rect_high = pygame.Rect(x + 20, y + 1, long - 40, 1)
        self.rect_left = pygame.Rect(x + 5, y + 5, 1, height - 10)
        self.rect_right = pygame.Rect(x + long - 5, y + 5, 1, height - 10)


# Class for Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.life_begin = 100
        self.life = 100
        self.velocity = 5
        self.jump_velocity = 20
        self.gravity = 2
        self.image = pygame.image.load('images/stickman.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 580
        self.pressed = {}
        self.time = pygame.time.get_ticks()
        self.move_up_nbr = 0

    # Movements functions :

    # Right
    def MoveRight(self):
        self.image = pygame.image.load('images/stickman_right.png')
        self.rect.x += self.velocity

    # Left
    def MoveLeft(self):
        self.image = pygame.image.load('images/stickman_left.png')
        self.rect.x -= self.velocity

    # Up
    def MoveUp(self):
        self.image = pygame.image.load('images/stickman_jump.png')
        self.move_up_nbr += 1
        self.rect.y -= self.jump_velocity
        return True

    # Down
    def MoveDown(self):
        self.rect.y += self.velocity
        return False

    # Gravity forces
    def Gravity(self):
        if self.rect.y + self.rect.height < 720:
            self.rect.y += self.gravity


# Class for the Exit Point
class Gate(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/gate.png')
        self.image = pygame.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Class for the Turret
class Gun(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/gun.png')
        self.image = pygame.transform.scale(self.image, (100, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 600
        self.all_bullet = pygame.sprite.Group()

    def launch_bullet(self):
        """Creates a bullet and stocks it in a sprite group"""
        if pygame.time.get_ticks() > 2000:
            self.all_bullet.add(Bullet(self))


# Class for Restart button
class Restart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/restart.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 350
        self.clickable_area = pygame.Rect(600, 350, 350, 150)


# Class for Quit button
class Quit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/quit.png')
        self.rect = self.image.get_rect()
        self.rect.x = 225
        self.rect.y = 350
        self.clickable_area = pygame.Rect(225, 350, 350, 150)

    def clique(self):
        pygame.quit()

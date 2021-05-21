from bullet import *
from Sounds import *
from Setting import resolution

#set variables for the screen resolution
ScreenWidth = resolution()[0]
ScreenHeight = resolution()[1]


# Class for walls
class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, long, height):
        super().__init__()
        # Loads the image and resizes it
        self.image = pygame.image.load('images/wall.jpg')
        self.image = pygame.transform.scale(self.image, (long, height))
        # Handles the screen coordinates
        self.rect = self.image.get_rect()
        self.x = x
        self.long = long
        self.height = height
        self.rect.x = x
        self.rect.y = y
        #rect for collisions with the player
        self.rect_bottom = pygame.Rect(self.rect.x + 5, self.rect.y + self.height - 2, self.long - 10, 1)
        self.rect_high = pygame.Rect(self.rect.x + 5, self.rect.y, self.long - 10, 1)
        self.rect_left = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 1, self.height - 10)
        self.rect_right = pygame.Rect(self.rect.x + self.long - 5, self.rect.y + 5, 1, self.height - 10)
        #variable for the move function
        self.right = False
        self.left = False
        self.compt = 0

    def Move(self):
        #wall moves right and when it's 200 more pixels, it moves to left
        if self.rect.x < self.x + 200 and self.left == True:
            self.compt += 1
            if self.compt % 2 == 0:
                self.rect.x += 1
                self.right = False
                #rect for collisions with the player
                self.rect_bottom = pygame.Rect(self.rect.x + 5, self.rect.y + self.height - 2, self.long - 10, 1)
                self.rect_high = pygame.Rect(self.rect.x + 5, self.rect.y, self.long - 10, 1)
                self.rect_left = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 1, self.height - 10)
                self.rect_right = pygame.Rect(self.rect.x + self.long - 5, self.rect.y + 5, 1, self.height - 10)
        elif self.rect.x == self.x + 200:
            self.right = True

        if self.right == True and self.rect.x > self.x:
            self.compt += 1
            if self.compt % 2 == 0:
                self.rect.x -= 1
                self.left = False
                # rect for collisions with the player
                self.rect_bottom = pygame.Rect(self.rect.x + 5, self.rect.y + self.height - 2, self.long - 10, 1)
                self.rect_high = pygame.Rect(self.rect.x + 5, self.rect.y, self.long - 10, 1)
                self.rect_left = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 1, self.height - 10)
                self.rect_right = pygame.Rect(self.rect.x + self.long - 5, self.rect.y + 5, 1, self.height - 10)
        elif self.rect.x == self.x:
            self.left = True


# Class for Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        """
        Sets all informations about the Player object and handles the sprite animations
        """
        super().__init__()
        # Velocity and life of the player
        self.life = 1000
        self.beginn_life = 1000
        self.velocity = round(ScreenHeight / 720 * 1.875)
        self.jump_velocity = round(ScreenHeight / 720 * 10.5)
        self.gravity = round(ScreenHeight / 720 * 1.9)
        # Image and coordinates
        self.image = pygame.image.load('images/run_right/rr4.png')
        self.image = pygame.transform.scale(self.image, (
            round(ScreenWidth/1080*self.image.get_rect().size[0] / 3), round(ScreenHeight/720*self.image.get_rect().size[1] /3 )))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 0
        # Player variables (for functions)
        self.pressed = {1073741904: False, 1073741903: False, 1073741906: False}
        self.time = pygame.time.get_ticks()
        self.move_up_nbr = 0
        self.move_up_nbr2 = 0
        self.nbr_image = 6
        self.nbr_image_left = 0
        self.nbr_image_left2 = 0
        self.nbr_image_right = 0
        self.nbr_image_right2 = 0
        self.nbr_image_j = 9
        self.nbr_image_jump = 0
        self.nbr_image_jump2 = 0
        self.direction = ""

    # Movements functions :

    # Right when player touches a wall
    def MoveRightTouching(self):
        self.direction = "right"
        self.nbr_image_right2 = str(self.nbr_image_right2)
        self.image = pygame.image.load(('images/run_right/rr' + self.nbr_image_right2 + '.png'))
        self.image = pygame.transform.scale(self.image, (
            round(ScreenWidth/1080*self.image.get_rect().size[0] / 3), round(ScreenHeight/720*self.image.get_rect().size[1] /3 )))
        self.rect.x += self.velocity
        self.nbr_image_right += 1

        # change images for the mouvements
        if self.nbr_image_right == 50:
            self.nbr_image_right = 0
        else:
            self.nbr_image_right2 = int(self.nbr_image_right / 10)

    # Right when player is flying
    def MoveRight(self):
        self.direction = "right"
        self.image = pygame.image.load('images/jr.png')
        self.image = pygame.transform.scale(self.image, (
            round(ScreenWidth/1080*self.image.get_rect().size[0] / 3), round(ScreenHeight/720*self.image.get_rect().size[1] / 3)))
        self.rect.x += self.velocity

    # Left when player touches a wall
    def MoveLeftTouching(self):
        self.direction = "left"
        self.nbr_image_left2 = str(self.nbr_image_left2)
        self.image = pygame.image.load('images/run_left/rl' + self.nbr_image_left2 + '.png')
        self.image = pygame.transform.scale(self.image, (
            round(ScreenWidth/1080*self.image.get_rect().size[0]/3), round(ScreenHeight/720*self.image.get_rect().size[1]/3)))
        self.rect.x -= self.velocity
        self.nbr_image_left += 1

        #change images for the mouvements
        if self.nbr_image_left == 50:
            self.nbr_image_left = 0
        else:
            self.nbr_image_left2 = int(self.nbr_image_left / 10)

    # Left when player is flying
    def MoveLeft(self):
        self.direction = "left"
        self.image = pygame.image.load('images/jl.png')
        self.image = pygame.transform.scale(self.image, (
            round(ScreenWidth/1080*self.image.get_rect().size[0] / 3), round(ScreenHeight/720*self.image.get_rect().size[1]/3)))
        self.rect.x -= self.velocity

    # Up
    def MoveUp(self):
        self.image = pygame.image.load('images/jl.png')
        self.image = pygame.transform.scale(self.image, (
            round(ScreenWidth/1080*self.image.get_rect().size[0] / 3), round(ScreenHeight/720*self.image.get_rect().size[1] /3)))
        self.move_up_nbr2 += 1
        self.rect.y -= self.jump_velocity


    # Down
    def MoveDown(self):
        self.rect.y += self.velocity

    # Gravity forces
    def Gravity(self):
        if self.rect.y + self.rect.height < ScreenHeight:
            self.rect.y += self.gravity


# Class for the Exit Point
class Gate(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # Load image and coordinates
        self.image = pygame.image.load('images/gate.jpg')
        self.image = pygame.transform.scale(self.image, (120, 180))
        self.image = pygame.transform.scale(self.image,
                                            (round(ScreenWidth / 1080 * 120), round(ScreenHeight / 720 * 180)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Collision with player
    def Collid(self):
        self.image = pygame.image.load('images/gate_open.jpg')
        self.image = pygame.transform.scale(self.image,
                                            (round(ScreenWidth / 1080 * 120), round(ScreenHeight / 720 * 180)))
        # Sound of the door
        self.mus = door("play")


# Class for the spike
class Pic(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # Load image and coordinates
        self.image = pygame.image.load('images/pic.jpg')
        self.image = pygame.transform.scale(self.image,
                                            (round(ScreenWidth / 1080 * 50), round(ScreenHeight / 720 * 30)))
        self.rect = self.image.get_rect()
        self.x = x
        self.rect.x = x
        self.rect.y = y
        # Rect for the collision with the player
        self.dead_rect = pygame.Rect(self.rect.x + 13, self.rect.y, 5, 5)
        self.compt = 0
        self.left = False
        self.right = False

    # Death collision for the player if contact ith the spike is made
    def dead(self, player):
        if player.rect.colliderect(self.dead_rect):
            player.life = 0
            self.mus = death("play")

    #Pic can move with this function
    def Move(self, v):
        # go right
        if self.rect.x < self.x + 200 and self.left == True:
            self.compt += 1
            if self.compt % v == 0:
                self.rect.x += 1
                self.right = False
                self.dead_rect = pygame.Rect(self.rect.x + 13, self.rect.y, 5, 5)
        elif self.rect.x == self.x + 200:
            self.right = True

        # go left
        if self.right == True and self.rect.x > self.x:
            self.compt += 1
            if self.compt % v == 0:
                self.rect.x -= 1
                self.left = False
                self.dead_rect = pygame.Rect(self.rect.x + 13, self.rect.y, 5, 5)
        elif self.rect.x == self.x:
            self.left = True


# Class for the Turret (Unused as of now)
class Gun(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # Load image and coordinates
        self.image = pygame.image.load('images/gun.png')
        self.image = pygame.transform.scale(self.image, (100, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 600
        self.all_bullet = pygame.sprite.Group()

    # launch bullet from the gun
    def launch_bullet(self):
        """Creates a bullet and stocks it in a sprite group"""
        self.all_bullet.add(Bullet())

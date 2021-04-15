from bullet import *

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
        self.rect_bottom = pygame.Rect(self.rect.x + 5, self.rect.y + self.height - 2, self.long - 10, 1)
        self.rect_high = pygame.Rect(self.rect.x + 5, self.rect.y, self.long - 10, 1)
        self.rect_left = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 1, self.height - 10)
        self.rect_right = pygame.Rect(self.rect.x + self.long - 5, self.rect.y + 5, 1, self.height - 10)
        self.right = False
        self.left = False
        self.compt = 0

    def Move(self):
        if self.rect.x <self.x +200 and self.left == True:
            self.compt+=1
            if self.compt%2 == 0:
                self.rect.x += 1
                self.right = False
                self.rect_bottom = pygame.Rect(self.rect.x + 5, self.rect.y + self.height - 2, self.long - 10, 1)
                self.rect_high = pygame.Rect(self.rect.x + 5, self.rect.y, self.long - 10, 1)
                self.rect_left = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 1, self.height - 10)
                self.rect_right = pygame.Rect(self.rect.x + self.long - 5, self.rect.y + 5, 1, self.height - 10)
        elif self.rect.x == self.x+200 :
            self.right = True

        if self.right == True and self.rect.x > self.x:
            self.compt+=1
            if self.compt%2 == 0:
                self.rect.x -= 1
                self.left = False
                self.rect_bottom = pygame.Rect(self.rect.x + 5, self.rect.y + self.height - 2, self.long - 10, 1)
                self.rect_high = pygame.Rect(self.rect.x + 5, self.rect.y, self.long - 10, 1)
                self.rect_left = pygame.Rect(self.rect.x + 5, self.rect.y + 5, 1, self.height - 10)
                self.rect_right = pygame.Rect(self.rect.x + self.long - 5, self.rect.y + 5, 1, self.height - 10)
        elif self.rect.x == self.x:
            self.left = True




# Class for Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.life = 1000
        self.beginn_life = 1000
        self.velocity = 1
        self.jump_velocity = 15
        self.gravity = 1
        self.image = pygame.image.load('images/stickman.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 0
        self.pressed = {1073741904: False, 1073741903: False, 1073741906: False}
        self.time = pygame.time.get_ticks()
        self.move_up_nbr = 0
        self.move_up_nbr2 = 0
        self.nbr_image=6
        self.nbr_image_left=0
        self.nbr_image_left2=0
        self.nbr_image_right = 0
        self.nbr_image_right2 = 0
        self.nbr_image_j = 9
        self.nbr_image_jump = 0
        self.nbr_image_jump2 = 0
        self.direction = ""
    # Movements functions :

    # Right
    def MoveRightTouching(self):
        self.direction = "right"
        self.nbr_image_right2 = str(self.nbr_image_right2)
        self.image = pygame.image.load(('images/run_right/rr' + self.nbr_image_right2 + '.png'))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().size[0] / 3), int(self.image.get_rect().size[1] / 3)))
        self.rect.x += self.velocity
        self.nbr_image_right += 1

        if self.nbr_image_right == 50:
            self.nbr_image_right = 0
        else:
            self.nbr_image_right2 = int(self.nbr_image_right / 10)

    def MoveRight(self):
        self.direction = "right"
        self.image = pygame.image.load('images/jr.png')
        self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().size[0]/3),int(self.image.get_rect().size[1]/3)))
        self.rect.x += self.velocity
    # Left
    def MoveLeftTouching(self):
        self.direction = "left"
        self.nbr_image_left2=str(self.nbr_image_left2)
        self.image = pygame.image.load('images/run_left/rl'+self.nbr_image_left2+'.png')
        self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().size[0]/3),int(self.image.get_rect().size[1]/3)))
        self.rect.x -= self.velocity
        self.nbr_image_left+=1

        if self.nbr_image_left == 50:
            self.nbr_image_left=0
        else:
            self.nbr_image_left2=int(self.nbr_image_left/10)

    def MoveLeft(self):
        self.direction = "left"
        self.image = pygame.image.load('images/jl.png')
        self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().size[0]/3),int(self.image.get_rect().size[1]/3)))
        self.rect.x -= self.velocity

    # Up
    def MoveUp(self):
        self.image = pygame.image.load('images/jl.png')
        self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().size[0]/3),int(self.image.get_rect().size[1]/3)))
        self.move_up_nbr += 1
        self.move_up_nbr2 +=1
        self.rect.y -= self.jump_velocity

    """def MoveUp(self):
        self.nbr_image_jump2 = str(self.nbr_image_jump2)
        self.image = pygame.image.load(('images/jump_right/j' + self.nbr_image_jump2 + '.png'))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_rect().size[0] / 3), int(self.image.get_rect().size[1] / 3)))

        self.rect.y -= self.jump_velocity
        self.nbr_image_right += 1

        self.move_up_nbr += 1
        self.move_up_nbr2 += 1

        if self.nbr_image_jump == 80:
            self.nbr_image_jump = 0
        else:
            self.nbr_image_jump2 = int(self.nbr_image_jump / 10)"""

    # Down
    def MoveDown(self):
        self.rect.y += self.velocity


    # Gravity forces
    def Gravity(self):
        if self.rect.y + self.rect.height < 720:
            self.rect.y += self.gravity

    #life bar
    def update_health_bar(self, surface):
        #def a color for the life bar (lite green)
        bar_color = (111,210,46)
        bar_color2 = (95, 95, 95)
        #def rect of the bar, and the dimensions
        bar_position = [self.rect.x, self.rect.y-20, self.life/10, 10]
        bar_position_begin = [self.rect.x, self.rect.y - 20, self.beginn_life / 10, 10]
        #draw the bar
        pygame.draw.rect(surface, bar_color2, bar_position_begin)
        pygame.draw.rect(surface, bar_color, bar_position)


# Class for the Exit Point
class Gate(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/gate.jpg')
        self.image = pygame.transform.scale(self.image, (120, 180))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def Collid(self):
        self.image = pygame.image.load('images/gate_open.jpg')
        self.image = pygame.transform.scale(self.image, (120, 180))
        self.mus = pygame.mixer.Sound("musique/door.mp3")
        self.mus.play()

# Class for the Pic
class Pic(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/pic.jpg')
        self.image = pygame.transform.scale(self.image, (50,30))
        self.rect = self.image.get_rect()
        self.x = x
        self.rect.x = x
        self.rect.y = y
        self.dead_rect = pygame.Rect(self.rect.x+13,self.rect.y,5,5)
        self.compt = 0
        self.left = False
        self.right = False
    #if player touche the pic, he will be dead
    def dead(self, player):
        if player.rect.colliderect(self.dead_rect):
            player.life=0
            self.mus = pygame.mixer.Sound("musique/dead.mp3")
            self.mus.set_volume(1.0)
            self.mus.play()

    def Move(self, v):
        if self.rect.x <self.x +200 and self.left == True:
            self.compt+=1
            if self.compt%v == 0:
                self.rect.x += 1
                self.right = False
                self.dead_rect = pygame.Rect(self.rect.x + 13, self.rect.y, 5, 5)
        elif self.rect.x == self.x+200 :
            self.right = True

        if self.right == True and self.rect.x > self.x:
            self.compt+=1
            if self.compt%v == 0:
                self.rect.x -= 1
                self.left = False
                self.dead_rect = pygame.Rect(self.rect.x + 13, self.rect.y, 5, 5)
        elif self.rect.x == self.x:
            self.left = True



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

    #launch bullet from the gun
    def launch_bullet(self):
        """Creates a bullet and stocks it in a sprite group"""
        self.all_bullet.add(Bullet(self))


"""# Class for Restart button
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
        pygame.quit()"""
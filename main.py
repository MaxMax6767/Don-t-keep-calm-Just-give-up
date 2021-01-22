import pygame
from objets import *
from bullet import *


def check_collision(sprite, group):
    """Checks for collisions between a sprite and a group of sprites"""
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


# Starts the Pygame Library
pygame.init()

# Creates a window and gives it a name
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Don't keep calm, Just give UP !")

# Loads Background
background = pygame.image.load('images/black.png')

# Creates a variable for text color
white_color = (255, 255, 255)

# Creates an object for the Player
player = Player()

# Add walls to the sprite group
wall = Wall(200, 150, 350, 30)
wall_bas = Wall(0, 690, 1080, 30)
wall_porte = Wall(800, 250, 250, 30)

# creates a door object
gate = Gate(900, 50)

# Loads the font
arial_font = pygame.font.SysFont("arial", 40, True, True)
texte_gagne = arial_font.render("You won !", True, white_color)

# Creates a turret object
gun = Gun(50, 50)

# Creates restart button object
restart = Restart()
quit = Quit()

# Boolean variable to have the player status to know if he's in the air
flying = False

# Game launching variable
launched = True

play = True
gate_collid = False
bullet = Bullet(120)

# Game loop
while launched:

    while play == True:
        #put images on the screen
        screen.blit(background, (0, 0))
        screen.blit(player.image, player.rect)
        screen.blit(gun.image, gun.rect)
        screen.blit(gate.image, gate.rect)
        screen.blit(wall_bas.image, wall_bas.rect)
        screen.blit(wall_porte.image, wall_porte.rect)
        screen.blit(wall.image, wall.rect)

        # Includes the bullets in the sprite group "all_bullets" for the object gun
        for bullet in gun.all_bullet:
            # Gives motion to the bullets
            bullet.move()
            # Deletes the bullets sprites when they touch the player or the screen border
            if bullet.rect.x > 1080:
                gun.all_bullet.remove(bullet)
            if bullet.rect.colliderect(player):
                gun.all_bullet.remove(bullet)

        # Checks if player is in a certain rectangle
        if player.rect.colliderect(pygame.Rect(140, 600, 1080, 100)):
            # adds the bullet to the sprite group gun
            gun.launch_bullet()

        # displays the bullet
        gun.all_bullet.draw(screen)

        # removes health to the player if he gets hit by a bullet
        if check_collision(player, gun.all_bullet):
            player.life -= 2

        print(player.life)

        # if the player if is not affected by a collision, he will go trough the floor
        if not (player.rect.colliderect(wall.rect_high) or player.rect.colliderect(
                wall_porte.rect_high) or player.rect.colliderect(wall_bas.rect_high)):
            player.Gravity()

        # right movement for right key pressed except if there's a wall on the right
        if player.pressed.get(pygame.K_RIGHT) and player.rect.x + player.rect.width < 1080:
            if not player.rect.colliderect(pygame.Rect(200, 160, 1, 18)) and not player.rect.colliderect(
                    pygame.Rect(800, 260, 1, 18)):
                player.MoveRight()

        # left movement for left key pressed except if there's a wall on the left
        if player.pressed.get(pygame.K_LEFT) and player.rect.x > 0:
            if not player.rect.colliderect(pygame.Rect(550, 160, 1, 18)):
                player.MoveLeft()

        # up movement for up key pressed except if there's a wall above
        if player.pressed.get(pygame.K_UP) and player.rect.y > 0:
            if not player.rect.colliderect(pygame.Rect(200, 178, 350, 1)) and not player.rect.colliderect(
                    pygame.Rect(800, 278, 350, 1)):
                flying = player.MoveUp()
                # if the loop is executed 15 times, it will stop movements to stop infinite jump
                if player.move_up_nbr % 15 == 0:
                    player.pressed[event.key] = False

        # down movement for down key pressed except if there's a wall below
        if player.pressed.get(pygame.K_DOWN) and player.rect.y + player.rect.height < 720:
            if not player.rect.colliderect(wall_bas.rect_high) or not player.rect.colliderect(
                    wall.rect_high) or not player.rect.colliderect(wall_porte.rect_high):
                player.MoveDown()

        # If player touches the bottom of a floor, he falls down
        if player.rect.colliderect(pygame.Rect(200, 180, 350, 1)) or player.rect.colliderect(
                pygame.Rect(800, 280, 300, 1)):
            player.Gravity()

        # If player touches Exit point, it ends the game and displays a message
        if player.rect.colliderect(gate):
            screen.blit(texte_gagne, (300, 300))
            gate_collid = True
            play = False
            break

        else:
            gate.image = pygame.image.load('images/gate.png')

        # If player live too low, game ends
        if player.life == 0:
            pygame.quit()

        # updates the screen
        pygame.display.flip()

        # event handling
        for event in pygame.event.get():
            # Game closing with ALT+F4 or with windows X
            if event.type == pygame.QUIT:
                launched = False
                pygame.quit()
                print("Shutting down")

            # Creates a list for player inputs
            if event.type == pygame.KEYDOWN:
                player.pressed[event.key] = True

            # If there's no new input, empty the list
            elif event.type == pygame.KEYUP:
                player.pressed[event.key] = False

    # Exit point collisions
    if gate_collid == True:
        gate.image = pygame.image.load('images/gate_open.jpg')
        screen.blit(texte_gagne, (300, 300))
        gate.image = pygame.image.load('images/gate_open.jpg')
        screen.blit(restart.image, restart.rect)
        screen.blit(quit.image, quit.rect)

    # Screen Update
    pygame.display.flip()

    # Events Handling
    for event in pygame.event.get():
        # Game closing with ALT + F4 or windows X
        if event.type == pygame.QUIT:
            launched = False
            pygame.quit()
            print("fermeture du jeu")


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if quit.clickable_area.collidepoint(event.pos):
                quit.clique()
            if restart.clickable_area.collidepoint(event.pos):
                play = True
                player.rect.x = 500
                player.rect.y = 300
                player.pressed = {}
                player.life = 100
                continue

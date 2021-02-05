import pygame
from objets import *
from bullet import *
import time


def game1():
    # Starts the Pygame Library
    pygame.init()

    # Creates a window and gives it a name
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Don't keep calm, Just give UP !")

    # Loads Background
    background = pygame.image.load('images/black.png')

    # Creates a variable for text color
    white_color = (255, 255, 255)

    # Loads the font
    arial_font = pygame.font.SysFont("arial", 40, True, True)
    texte_gagne = arial_font.render("You won !", True, white_color)
    texte_lose = arial_font.render("You're dead... ", True, white_color)


    # Creates an object for the Player
    player = Player()

    # Add walls to the sprite group
    wall = Wall(200, 150, 350, 30)
    wall_bas = Wall(0, 690, 1080, 30)
    wall_porte = Wall(800, 250, 250, 30)

    # creates a door object
    gate = Gate(900, 80)

    #creates a pic object
    pic = Pic(250,140)

    # Creates a turret object
    gun = Gun(50, 50)

    # Creates restart button object
    restart = Restart()
    quit = Quit()

    # Game launching variable
    launched = True

    play = True
    win = False
    bullet = Bullet(120)

    # time at the begining of the game
    time1 = time.perf_counter()

    #time waiting to launch the first bullet
    time_launch_bullet = time.time() + 1

    # Game loop
    while launched:

        while play == True:
            #put images on the screen
            screen.blit(background, (0, 0))
            screen.blit(gun.image, gun.rect)
            screen.blit(gate.image, gate.rect)
            screen.blit(wall_bas.image, wall_bas.rect)
            screen.blit(wall_porte.image, wall_porte.rect)
            screen.blit(wall.image, wall.rect)
            screen.blit(pic.image, pic.rect)
            screen.blit(player.image, player.rect)

            # Includes the bullets in the sprite group "all_bullets" for the object gun
            for bullet in gun.all_bullet:
                # Gives motion to the bullets
                bullet.move()


                # Deletes the bullets sprites when they touch the player or the screen border
                if bullet.rect.x > 1080:
                    gun.all_bullet.remove(bullet)
                if bullet.rect.colliderect(player):
                    # removes health to the player if he gets hit by a bullet
                    player.life += bullet.life
                    gun.all_bullet.remove(bullet)

            # Checks if player is in a certain rectangle
            if player.rect.colliderect(pygame.Rect(140, 600, 1080, 100)):
                #lanch bullet after 1s
                if time.time()>time_launch_bullet:
                    # adds the bullet to the sprite group gun
                    gun.launch_bullet()

            # displays the bullet
            gun.all_bullet.draw(screen)

            # create and show the time
            time_run = int(time.perf_counter())
            time_run_str = str(time_run)
            show_time = arial_font.render(time_run_str, True, white_color)
            screen.blit(show_time, (0, 0))

            # if the player if is not affected by a collision, he will go trough the floor
            if not (player.rect.colliderect(wall.rect_high) or player.rect.colliderect(wall_porte.rect_high) or player.rect.colliderect(wall_bas.rect_high)):
                player.Gravity()

            # right movement for right key pressed except if there's a wall on the right
            if player.pressed.get(pygame.K_RIGHT) and player.rect.x + player.rect.width < 1080:
                if not player.rect.colliderect(wall.rect_left) and not player.rect.colliderect(wall_porte.rect_left):
                    player.MoveRight()

            # left movement for left key pressed except if there's a wall on the left
            if player.pressed.get(pygame.K_LEFT) and player.rect.x > 0:
                if not player.rect.colliderect(wall.rect_right):
                    player.MoveLeft()

            # up movement for up key pressed except if there's a wall above
            if player.pressed.get(pygame.K_UP) and player.rect.y > 0:
                if not player.rect.colliderect(wall.rect_bottom) and not player.rect.colliderect(pygame.Rect(800, 278, 350, 1)):
                    player.MoveUp()
                    # if the loop is executed 15 times, it will stop movements to stop infinite jump
                    """if player.move_up_nbr % 10 == 0:
                        player.pressed[event.key] = False"""

            # down movement for down key pressed except if there's a wall below
            if player.pressed.get(pygame.K_DOWN) and player.rect.y + player.rect.height < 720:
                if not player.rect.colliderect(wall_bas.rect_high) or not player.rect.colliderect(wall.rect_high) or not player.rect.colliderect(wall_porte.rect_high):
                    player.MoveDown()

            # If player touches the bottom of a floor, he falls down
            if player.rect.colliderect(pygame.Rect(200, 180, 350, 1)) or player.rect.colliderect(pygame.Rect(800, 280, 300, 1)):
                player.Gravity()

            # If player touches the Pic he dies
            if player.rect.colliderect(pic.dead_rect):
                print("he touches the pic")
                player.life=0

            # If player touches Exit point, it ends the game and displays a message
            if player.rect.colliderect(gate):
                win = True
                play = False
                break


            # If player live too low, game ends
            if player.life == 0:
                play=False
                break

            # draw the life bar
            player.update_health_bar(screen)

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
                elif event.type == pygame.MOUSEMOTION:
                    # récupére la position de la souris et la print
                    print("{}".format(event.pos))

        # Exit point collisions
        if win == True :
            break
        if player.life == 0:
            end = time.time()+1.5
            while end>time.time():
                screen.blit(texte_lose, (300, 300))
                # Screen Update
                pygame.display.flip()
            return False, False

        # Events Handling
        for event in pygame.event.get():
            # Game closing with ALT + F4 or windows X
            if event.type == pygame.QUIT:
                launched = False
                pygame.quit()
                print("game closed")

    time2 = time.perf_counter()

    #if the player touch the door
    if win==True:
        end = time.time()+2
        # During 2 seconds we can see the door open and a win text
        while time.time()<end:
            gate.image = pygame.image.load('images/gate_open.jpg')
            gate.image = pygame.transform.scale(gate.image, (120, 170))
            screen.blit(gate.image, gate.rect)
            screen.blit(texte_gagne, (300, 300))

            pygame.display.flip()

            for event in pygame.event.get():
                # Game closing with ALT + F4 or windows X
                if event.type == pygame.QUIT:
                    end = False
                    pygame.quit()
                    print("game closed")

        #return True (player win) and the time used to finish the level
        return True, time2 - time1
from objets import *
from bullet import *
import time


def game2():
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
    arial_font2 = pygame.font.SysFont("arial", 200, True, white_color)
    texte_gagne = arial_font.render("You won !", True, white_color)
    texte_lose = arial_font.render("You're dead... ", True, white_color)


    # Creates an object for the Player
    player = Player()

    # Add walls to the sprite group
    wall = Wall(120, 370, 200, 15)
    wall_bas = Wall(0, 700, 1080, 20)
    wall_porte = Wall(800, 245, 250, 20)

    # creates a door object
    gate = Gate(900, 65)

    #creates a pic object
    pic = Pic(280,670)
    pic2 = Pic(450,670)
    pic3 = Pic(620, 670)

    # Game launching variable
    launched = True
    play = True
    win = False

    # time at the begining of the game
    time1 = time.perf_counter()

    #time waiting to launch the first bullet
    time_launch_bullet = time.time() + 1

    # Game loop
    while launched:

        while play == True:
            #put images on the screen
            screen.blit(background, (0, 0))
            screen.blit(gate.image, gate.rect)
            screen.blit(wall_bas.image, wall_bas.rect)
            screen.blit(wall_porte.image, wall_porte.rect)
            screen.blit(wall.image, wall.rect)
            screen.blit(pic.image, pic.rect)
            screen.blit(pic2.image, pic2.rect)
            screen.blit(pic3.image, pic3.rect)
            screen.blit(player.image, player.rect)



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
                if not player.rect.colliderect(wall.rect_bottom) and not player.rect.colliderect(wall_porte.rect_bottom):
                    #if player don't fly so much, he can fly
                    if player.move_up_nbr2<30:
                        player.MoveUp()
                    # if the loop is executed 15 times, it will stop movements to stop infinite jump
                    if player.move_up_nbr % 15 == 0:
                        player.pressed[event.key] = False

            # down movement for down key pressed except if there's a wall below
            if player.pressed.get(pygame.K_DOWN) and player.rect.y + player.rect.height < 720:
                if not player.rect.colliderect(wall_bas.rect_high) and not player.rect.colliderect(wall.rect_high) and not player.rect.colliderect(wall_porte.rect_high):
                    player.MoveDown()

            # If player touches the bottom of a floor, he falls down
            if player.rect.colliderect(wall.rect_bottom) or player.rect.colliderect(wall_porte.rect_bottom):
                player.Gravity()

            #if player touch a pic, he's dead! ;-)
            pic.dead(player)
            pic2.dead(player)
            pic3.dead(player)

            #if player touch a wall, he can fly a new time
            if player.rect.colliderect(wall_bas.rect_high) or player.rect.colliderect(wall.rect_high) or player.rect.colliderect(wall_porte.rect_high):
                player.move_up_nbr2 = 0

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
                    # print the position of the mouse
                    print(event.pos)

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
            gate.image = pygame.transform.scale(gate.image, (120, 180))
            screen.blit(gate.image, gate.rect)
            screen.blit(texte_gagne, (300, 300))

            pygame.display.flip()

            for event in pygame.event.get():
                # Game closing with ALT + F4 or windows X
                if event.type == pygame.QUIT:
                    end = False
                    pygame.quit()
                    print("game closed")

            level_up_time = time.time() + 1
            while time.time() < level_up_time:
                texte_level_up = arial_font2.render("level UP!", True, white_color)
                screen.fill((0, 0, 0))
                screen.blit(texte_level_up, (120, 200))
                pygame.display.flip()
                for event in pygame.event.get():
                    # Game closing with ALT + F4 or windows X
                    if event.type == pygame.QUIT:
                        end = False
                        pygame.quit()
                        print("game closed")

        #return True (player win) and the time used to finish the level
        return True, time2 - time1

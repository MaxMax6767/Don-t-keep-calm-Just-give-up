from objets import *
from functions import *
import time
from Sounds import music
from Setting import resolution
import sys
import os


# Syntax simplification for the resolutions (It's used frequently)
ScreenWidth = resolution()[0]
ScreenHeight = resolution()[1]


def game1():
    global change  # Global variable for the end of the level
    music("play")  # Starts the music
    pygame.init()  # Starts the Pygame Library

    screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))  # Create a window and sets screen size
    pygame.display.set_caption("Don't keep calm, Just give UP !")  # Sets window name

    background = pygame.image.load(resource_path('images/black.png')) # Loads Background (in thos case a plane black picture)

    white_color = (255, 255, 255)  # Syntax simplification for white color

    # Initialises the fonts used
    arial_font = pygame.font.SysFont("arial", 40, True, True)
    arial_font2 = pygame.font.SysFont("arial", round(ScreenWidth/1080*200), True, white_color)
    texte_gagne = arial_font.render("You won !", True, white_color)
    texte_lose = arial_font.render("You're dead... ", True, white_color)

    player = Player()  # Creates the player object

    # Add walls to the sprite group (Using screen size adaptive method)
    wall_begin = Wall(round(ScreenWidth/1080*60), round(ScreenHeight/720*170), round(ScreenWidth/1080*150), round(ScreenHeight/720*15))
    wall2 = Wall(round(ScreenWidth/1080*580), round(ScreenHeight/720*500), round(ScreenWidth/1080*200), round(ScreenHeight/720*15))
    wall_bas = Wall(0, (ScreenHeight-round(ScreenHeight/720*15)), ScreenWidth, round(ScreenHeight/720*15))
    wall3 = Wall(10000, 0, 1, 1)

    # creates a door object
    gate = Gate(round(ScreenWidth/1080*930), round(ScreenHeight/720*550))  # Places the gate at a given coordinate depending on the resolution gotout of the settings
    gate_collid = False  # Sets the collision to false by default

    #creates a spike object
    pic = Pic(round(ScreenWidth/1080*620), ScreenHeight-(round(ScreenHeight/720*15+round(ScreenHeight/720*30))))
    pic2 = Pic(round(ScreenWidth/1080*820), ScreenHeight-(round(ScreenHeight/720*15+round(ScreenHeight/720*30))))

    # Game launching variable
    launched = True
    play = True
    win = False

    time1 = time.perf_counter()  # Time counter

    # Game loop
    while launched:

        while play:

            # Display images on the screen
            screen.blit(background, (0, 0))
            screen.blit(gate.image, gate.rect)
            screen.blit(pic.image, pic.rect)
            screen.blit(pic2.image, pic2.rect)
            screen.blit(wall_bas.image, wall_bas.rect)
            screen.blit(wall2.image, wall2.rect)
            screen.blit(wall_begin.image, wall_begin.rect)
            screen.blit(player.image, player.rect)

            # Create and show the time
            time_run = int(time.perf_counter())
            time_run_str = str(time_run)
            show_time = arial_font.render(time_run_str, True, white_color)
            screen.blit(show_time, (0, 0))

            mouvements(player, wall_begin, wall_bas, wall2, wall3)  # Initialises player movements

            # Checks for collision with player
            pic.dead(player)
            pic2.dead(player)

            # Resets player juming ability if he touches floor
            if player.rect.colliderect(wall_bas.rect_high) or player.rect.colliderect(wall_begin.rect_high) or player.rect.colliderect(wall2.rect_high):
                player.move_up_nbr2 = 0

            # If player touches Exit point, it ends the game and displays a message
            if player.rect.colliderect(gate) and gate_collid == False:
                gate.Collid()
                gate_collid = True
                change = time.time() + 1
            if gate_collid == True and player.rect.colliderect(gate):
                if change < time.time():
                    win = True
                    play = False
                    break

            # Game end if player is dead
            if player.life == 0:
                play=False
                break

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
        if win:
            break
        if player.life == 0:
            end = time.time()+1.5
            while end>time.time():
                screen.blit(texte_lose, (round(ScreenWidth/1080*300), round(ScreenHeight/720*300)))
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
            gate.image = pygame.image.load(resource_path('images/gate_open.jpg'))
            gate.image = pygame.transform.scale(gate.image, (round(ScreenWidth/1080*120), round(ScreenHeight/720*180)))
            screen.blit(gate.image, gate.rect)
            screen.blit(texte_gagne, (round(ScreenWidth/1080*300), round(ScreenHeight/720*300)))

            pygame.display.flip()

            for event in pygame.event.get():
                # Game closing with ALT + F4 or windows X
                if event.type == pygame.QUIT:
                    end = False
                    pygame.quit()
                    print("game closed")

            level_up_time = time.time() + 1
            while time.time() < level_up_time:
                texte_level_up = arial_font2.render("Level UP!", True, white_color)
                screen.fill((0, 0, 0))
                screen.blit(texte_level_up, (round(ScreenWidth/1080*100), round(ScreenHeight/720*200)))
                pygame.display.flip()
                for event in pygame.event.get():
                    # Game closing with ALT + F4 or windows X
                    if event.type == pygame.QUIT:
                        end = False
                        pygame.quit()
                        print("game closed")

        #return True (player win) and the time used to finish the level
        return True, time2 - time1

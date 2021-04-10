import pygame

def mouvements(player, wall, wall_bas, wall_porte):

    # if the player if is not affected by a collision, he will go trough the floor
    if not (player.rect.colliderect(wall.rect_high) or player.rect.colliderect(wall_porte.rect_high) or player.rect.colliderect(wall_bas.rect_high)):
        player.Gravity()
        if player.pressed.get(pygame.K_RIGHT) and player.rect.x + player.rect.width < 1080:
            if not player.rect.colliderect(wall.rect_left) and not player.rect.colliderect(wall_porte.rect_left):
                player.MoveRight()
        elif player.pressed.get(pygame.K_LEFT) and player.rect.x > 0:
            if not player.rect.colliderect(wall.rect_right):
                player.MoveLeft()
        else:
            if player.direction == "left":
                player.image = pygame.image.load('images/run_left/rl4.png')
                player.image = pygame.transform.scale(player.image, (100,100))
            else:
                player.image = pygame.image.load('images/run_right/rr4.png')
                player.image = pygame.transform.scale(player.image, (100, 100))

    # right movement for right key pressed except if there's a wall on the right
    elif player.pressed.get(pygame.K_RIGHT) and player.rect.x + player.rect.width < 1080:
        if not player.rect.colliderect(wall.rect_left) and not player.rect.colliderect(wall_porte.rect_left):
            player.MoveRightTouching()
    # left movement for left key pressed except if there's a wall on the left
    elif player.pressed.get(pygame.K_LEFT) and player.rect.x > 0:
        if not player.rect.colliderect(wall.rect_right):
            player.MoveLeftTouching()


    # If player touches the bottom of a floor, he falls down
    if player.rect.colliderect(wall.rect_bottom) or player.rect.colliderect(wall_porte.rect_bottom):
        player.Gravity()

       # up movement for up key pressed except if there's a wall above
    if player.pressed.get(pygame.K_UP) and player.rect.y > 0:
        if not player.rect.colliderect(wall.rect_bottom) and not player.rect.colliderect(wall_porte.rect_bottom):
            # if player don't fly so much, he can fly
            if player.move_up_nbr2 < 30:
                player.MoveUp()
            # if the loop is executed 15 times, it will stop movements to stop infinite jump
            if player.move_up_nbr % 15 == 0:
                player.pressed[1073741906]=False

    # down movement for down key pressed except if there's a wall below
    if player.pressed.get(pygame.K_DOWN) and player.rect.y + player.rect.height < 720:
        if not player.rect.colliderect(wall_bas.rect_high) and not player.rect.colliderect(
                wall.rect_high) and not player.rect.colliderect(wall_porte.rect_high):
            player.MoveDown()

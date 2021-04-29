import pygame
from Setting import resolution
from Setting import moveLeft, moveDown, moveRight, moveUp

ScreenWidth = resolution()[0]
ScreenHeight = resolution()[1]


def mouvements(player, wall, wall_bas, wall_porte, wall3):

    # if the player if is not affected by a collision, he will go trough the floor
    if not (player.rect.colliderect(wall.rect_high) or player.rect.colliderect(wall_porte.rect_high) or player.rect.colliderect(wall_bas.rect_high) or player.rect.colliderect(wall3.rect_high)):
        player.Gravity()
        if player.pressed.get(moveRight()) and player.rect.x + player.rect.width < ScreenWidth:
            if not player.rect.colliderect(wall.rect_left) or not player.rect.colliderect(wall_porte.rect_left) or not player.rect.colliderect(wall3.rect_left):
                player.MoveRight()
        elif player.pressed.get(moveLeft()) and player.rect.x > 0:
            if not player.rect.colliderect(wall.rect_right) and not player.rect.colliderect(wall3.rect_right):
                player.MoveLeft()
        else:
            if player.direction == "left":
                player.image = pygame.image.load('images/run_left/rl4.png')
                player.image = pygame.transform.scale(player.image, (round(ScreenWidth/1080*100),round(ScreenHeight/720*100)))
            else:
                player.image = pygame.image.load('images/run_right/rr4.png')
                player.image = pygame.transform.scale(player.image, (round(ScreenWidth/1080*100), round(ScreenHeight/720*100)))

    # right movement for right key pressed except if there's a wall on the right
    elif player.pressed.get(moveRight()) and player.rect.x + player.rect.width < ScreenWidth:
        if not player.rect.colliderect(wall.rect_left) and not player.rect.colliderect(wall_porte.rect_left) and not player.rect.colliderect(wall3.rect_left):
            player.MoveRightTouching()
    # left movement for left key pressed except if there's a wall on the left
    elif player.pressed.get(moveLeft()) and player.rect.x > 0:
        if not player.rect.colliderect(wall.rect_right) and not player.rect.colliderect(wall_porte.rect_right):
            player.MoveLeftTouching()


    # If player touches the bottom of a floor, he falls down
    if player.rect.colliderect(wall.rect_bottom) or player.rect.colliderect(wall_porte.rect_bottom) or player.rect.colliderect(wall3.rect_right):
        player.Gravity()

       # up movement for up key pressed except if there's a wall above
    if player.pressed.get(moveUp()) and player.rect.y > 0:
        if not player.rect.colliderect(wall.rect_bottom) and not player.rect.colliderect(wall_porte.rect_bottom) and not player.rect.colliderect(wall3.rect_bottom):
            # if player don't fly so much, he can fly
            if player.move_up_nbr2 < 30 and player.move_up_nbr<2:
                player.MoveUp()
            # if the loop is executed 15 times, it will stop movements to stop infinite jump
            if player.move_up_nbr2 % 30 == 0 :
                player.pressed[1073741906] = False
                player.move_up_nbr +=1
                player.move_up_nbr2 = 0

    # down movement for down key pressed except if there's a wall below
    if player.pressed.get(moveDown()) and player.rect.y + player.rect.height < ScreenHeight:
        if not player.rect.colliderect(wall_bas.rect_high) and not player.rect.colliderect(
                wall.rect_high) and not player.rect.colliderect(wall_porte.rect_high) and not player.rect.colliderect(wall3.rect_high):
            player.MoveDown()
    if player.rect.colliderect(wall_bas.rect_high) or player.rect.colliderect(
                wall.rect_high) or player.rect.colliderect(wall_porte.rect_high) or player.rect.colliderect(wall3.rect_high):
        player.move_up_nbr = 0
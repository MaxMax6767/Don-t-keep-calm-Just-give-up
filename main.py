import settings
import pygame

r, g, b = 255, 0, 0

pygame.init()
pygame.init()
canvas = pygame.Surface((settings.width(), settings.height()))
window = pygame.display.set_mode((settings.width(), settings.height()))
running = True
clock = pygame.time.Clock()

while running:
    if r > 0 and b == 0:
        r = r-1
        g = g+1
    if g > 0 and r == 0:
        g = g-1
        b = b+1
    if b > 0 and g == 0:
        r = r+1
        b = b-1

    clock.tick(settings.FPS())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    canvas.fill((r, g, b))
    window.blit(canvas, (0, 0))
    pygame.display.update()

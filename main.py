import settings
import pygame


pygame.init()
pygame.init()
canvas = pygame.Surface((settings.width(), settings.height()))
window = pygame.display.set_mode((settings.width(), settings.height()))
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(settings.FPS())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    canvas.fill((0, 180, 240))
    window.blit(canvas, (0, 0))
    pygame.display.update()

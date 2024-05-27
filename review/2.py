import pygame
from cat import Cat
screen = pygame.display.set_mode((480,360))
cat = Cat(480,360)


runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    screen.fill((255,255,255))
    cat.draw(screen)
    pygame.display.update()
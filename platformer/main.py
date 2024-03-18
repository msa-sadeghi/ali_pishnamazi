import pygame

screen_width = 1000
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    
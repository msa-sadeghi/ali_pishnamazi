import pygame
from world import World
from level_creator import world_data
screen_width = 1000
screen_height = 700
FPS = 60
game_world = World(world_data)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    
import pygame
from world import World
from level_creator import world_data
from player import Player

blob_group = pygame.sprite.Group()
hidden_grass_group = pygame.sprite.Group()
game_player = Player()
screen_width = 1000
screen_height = 700
FPS = 60
game_world = World(world_data, blob_group, hidden_grass_group)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw(screen) 
    if game_player.alive:   
        game_player.move(game_world.tiles, blob_group, hidden_grass_group)
    game_player.draw(screen)
    blob_group.draw(screen)
    if game_player.show_grass:
        hidden_grass_group.draw(screen)
    blob_group.update()
    pygame.display.update()
    clock.tick(FPS)
    
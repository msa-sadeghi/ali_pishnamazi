import pygame
from world import World
from level_creator import world_data
from player import Player
from button import Button
pygame.init()
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("error", "i did'nt find any joystick")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()




restart_img = pygame.image.load("assets/restart_btn.png")

blob_group = pygame.sprite.Group()
hidden_grass_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
game_player = Player()
screen_width = 1000
screen_height = 700
restart_btn = Button(restart_img, screen_width/2 , screen_height/2)
FPS = 60
game_world = World(world_data, blob_group, hidden_grass_group, door_group, lava_group)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
while running:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
    game_world.draw(screen) 
    if game_player.alive:   
        game_player.move(game_world.tiles, blob_group, hidden_grass_group, door_group, lava_group)
    else:
        restart_btn.draw(screen)
        if restart_btn.check_click():
            game_player.reset()
    
    if joystick_count != 0:
        h = my_joystick.get_axis(0)
        v = my_joystick.get_axis(1)
        game_player.rect.x += 10 * h
        game_player.rect.y += 10 * v
    
    game_player.draw(screen)
    blob_group.draw(screen)
    if game_player.show_grass:
        hidden_grass_group.draw(screen)
    blob_group.update()
    # door_group.draw(screen)
    lava_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    
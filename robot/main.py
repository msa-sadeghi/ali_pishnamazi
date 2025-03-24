import pygame
from player import Player
from rock import Rock
pygame.init()



rock_group = pygame.sprite.Group()

width = 1000
height = 600

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
fps = 60

rock = Rock()
rock_group.add(rock)
bullet_group = pygame.sprite.Group()
my_player = Player(100, 300)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_player.in_air:
        my_player.change_animation("Jump")
    elif my_player.sliding:
        my_player.change_animation("Slide")
    elif my_player.run_shoot:
        my_player.change_animation('RunShoot')
    elif my_player.idle:
        my_player.change_animation("Idle")

    else:
        my_player.change_animation("Run")
 
    
    screen.fill("black")
   
    my_player.draw(screen)
    my_player.move(bullet_group)
    rock_group.update(my_player)
    rock_group.draw(screen)
    bullet_group.update()
    bullet_group.draw(screen)
    print(my_player.health)
    pygame.display.update()
    clock.tick(fps)
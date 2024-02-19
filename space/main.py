from constants import *
from player import Player

player_bullet_group = pygame.sprite.Group()
my_player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire(player_bullet_group)
    screen.fill((0,0,0))
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    my_player.move()
    my_player.draw()
    pygame.display.update()
    clock.tick(FPS)
    
    
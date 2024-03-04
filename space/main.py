from constants import *
from player import Player
from chick import Chick

player_bullet_group = pygame.sprite.Group()
chick_group = pygame.sprite.Group()
egg_group = pygame.sprite.Group()
my_player = Player()


def chick_spawn():
    for i in range(4):
        for k in range(8):
            Chick(k * 96 + 200, i * 96 + 60, chick_group)
            
chick_spawn()

level = 1

def check_edge_collisions():
    on_edge = False
    for chick in chick_group:
        if chick.rect.left < 0 or chick.rect.right > SCREEN_WIDTH:
            on_edge = True
            break
    if on_edge:
        for chick in chick_group:
            chick.direction *= -1
            chick.rect.y += 10 * level
            
def check_bullet_collisions():
    if pygame.sprite.groupcollide(player_bullet_group, chick_group, True, True):
        pass
    if pygame.sprite.spritecollide(my_player, egg_group, True):
        pass
    if pygame.sprite.groupcollide(player_bullet_group, egg_group, True, True):
        pass
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire(player_bullet_group)
    check_edge_collisions()
    check_bullet_collisions()
    screen.fill((0,0,0))
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    chick_group.update(egg_group)
    chick_group.draw(screen)
    egg_group.update()
    egg_group.draw(screen)
    my_player.move()
    my_player.draw()
    pygame.display.update()
    clock.tick(FPS)
    
    
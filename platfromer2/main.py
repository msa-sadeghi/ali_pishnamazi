import pygame
import os
from soldier import Solider
from healthbar import HealthBar
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()



player = Solider("player", 100, 300, 20, 10)
my_healthbar = HealthBar(10,20, player.health, player.max_health)

enemy1 = Solider("enemy", 600, 300, 10, 0)
# enemy2 = Solider("enemy", 400, 300, 0, 0)
enemy_group.add(enemy1)
# enemy_group.add(enemy2)
moving_left = False
moving_right = False
ai_moving_left, ai_moving_right = (True, False)
shoot = False
grenade = False
grenade_thrown = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
                player.idle = False
            if event.key == pygame.K_RIGHT:
                moving_right = True
                player.idle = False
            if event.key == pygame.K_SPACE:
                player.jump = True
            if event.key == pygame.K_s:
                shoot = True
            if event.key == pygame.K_g:
                grenade = True
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
                player.idle = True
            if event.key == pygame.K_RIGHT:
                moving_right = False
                player.idle = True
            if event.key == pygame.K_SPACE:
                player.jump = False
            if event.key == pygame.K_s:
                shoot = False
            if event.key == pygame.K_g:
                grenade = False
                grenade_thrown = False
        
    screen.fill((0,0,0))
    my_healthbar.draw(screen, player.health)
    player.draw(screen) 
    if player.alive:
        if shoot:
            player.shoot("bullet", player_bullet_group)
            shoot = False
        elif grenade and not grenade_thrown:
            player.shoot("grenade", grenade_group)
            grenade_thrown = True
        if moving_left or moving_right:
            player.set_action(1)
        elif player.in_air:
            player.set_action(2)
            
        else:
            player.set_action(0)
        player.move(moving_left, moving_right)  
    enemy_bullet_group.update(player, enemy_group, player_bullet_group,enemy_bullet_group)
    player_bullet_group.update(player, enemy_group, player_bullet_group,enemy_bullet_group)
    
    player_bullet_group.draw(screen)
    enemy_bullet_group.draw(screen)
    grenade_group.update(explosion_group, player, enemy_group)
    grenade_group.draw(screen)
    player.update()
     
    # enemy_group.update()
    for enemy in enemy_group:
        enemy.update()
        
        enemy.draw(screen)
        ai_moving_left, ai_moving_right = enemy.ai(player, enemy_bullet_group, ai_moving_left, ai_moving_right, screen)
         
    explosion_group.update()
    explosion_group.draw(screen)
    pygame.display.update()
    
    
    clock.tick(FPS)

os.system("cls")
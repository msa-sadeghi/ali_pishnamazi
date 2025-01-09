import pygame
from castle import Castle
from enemy import Enemy
pygame.init()

screen_width = 800
screen_height = 600

enemy_group = pygame.sprite.Group()
enemy = Enemy("goblin", 100, 350, 100, 10, 10,1)
enemy_group.add(enemy)
screen = pygame.display.set_mode((screen_width, screen_height))
bg_image = pygame.image.load("assets/img/bg.png")
FPS = 60
clock = pygame.time.Clock()

castle = Castle(screen_width - 330, screen_height-400)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0,0))  
    castle.draw(screen) 
    enemy_group.draw(screen)
    enemy_group.update()     
    pygame.display.update()
    clock.tick(FPS)
    

    
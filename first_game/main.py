import pygame
import random
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60
score = 0
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

chick_image = pygame.image.load("assets/chick.png")
chick_rect = chick_image.get_rect()
chick_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

salad_image = pygame.image.load("assets/salad.png")
salad_rect = salad_image.get_rect()
salad_rect.bottom = SCREEN_HEIGHT
salad_rect.centerx = random.randint(32, SCREEN_WIDTH-32)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        chick_rect.y -= 5
    if keys[pygame.K_DOWN]:
        chick_rect.y += 5
    if keys[pygame.K_LEFT]:
        chick_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        chick_rect.x += 5

    salad_rect.y -= 5
    if salad_rect.bottom <= 0:
        salad_rect.bottom = SCREEN_HEIGHT
        salad_rect.centerx = random.randint(32, SCREEN_WIDTH-32)

    if chick_rect.colliderect(salad_rect):
        salad_rect.bottom = SCREEN_HEIGHT
        salad_rect.centerx = random.randint(32, SCREEN_WIDTH - 32)
        score += 1

    screen.fill((0,0,0))
    screen.blit(chick_image, chick_rect)
    screen.blit(salad_image, salad_rect)
    pygame.display.update()
    clock.tick(FPS)

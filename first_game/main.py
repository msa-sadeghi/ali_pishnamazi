import pygame
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

chick_image = pygame.image.load("assets/chick.png")
chick_rect = chick_image.get_rect()
chick_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

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
    screen.fill((0,0,0))
    screen.blit(chick_image, chick_rect)
    pygame.display.update()
    clock.tick(FPS)

import random
import pygame
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60
score = 0
lives = 3
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

chick_image = pygame.image.load("assets/chick.png")
chick_rect = chick_image.get_rect()
chick_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

salad_image = pygame.image.load("assets/salad.png")
salad_rect = salad_image.get_rect()
salad_rect.bottom = SCREEN_HEIGHT
salad_rect.centerx = random.randint(32, SCREEN_WIDTH-32)


game_font = pygame.font.Font("assets/font.otf",34)
score_text= game_font.render(f"Score:{score}", True, (190,10,180))
score_rect = score_text.get_rect(top=0, centerx=SCREEN_WIDTH/2)
lives_text= game_font.render(f"lives:{lives}", True, (190,10,180))
lives_rect = lives_text.get_rect(topleft=(0,0))

pygame.mixer.music.load("assets/music.wav")
pygame.mixer.music.play(-1)

catch_sound = pygame.mixer.Sound("assets/coin.wav")


def game_over():
    pygame.mixer.music.stop()
    global running, score, lives
    game_over_text = game_font.render("Game Over, Press Enter to play again", True, (200,30,210))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    

    screen.fill((0,0,0))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.update()
    
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(-1)
                    score = 0
                    lives = 3
                    paused = False
                    
            
        
    


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

    if chick_rect.colliderect(salad_rect):
        salad_rect.bottom = SCREEN_HEIGHT
        salad_rect.centerx = random.randint(32, SCREEN_WIDTH - 32)
        score += 1
        catch_sound.play()
        
    salad_rect.y -= 5
    if salad_rect.bottom <= 0:
        salad_rect.bottom = SCREEN_HEIGHT
        salad_rect.centerx = random.randint(32, SCREEN_WIDTH-32)
        lives -= 1
        if lives <= 0:
            game_over()

        
    
    score_text= game_font.render(f"Score:{score}", True, (190,10,180))
    lives_text= game_font.render(f"lives:{lives}", True, (190,10,180))
    

    screen.fill((0,0,0))
    screen.blit(chick_image, chick_rect)
    screen.blit(salad_image, salad_rect)
    screen.blit(score_text, score_rect)
    screen.blit(lives_text, lives_rect)
    pygame.display.update()
    clock.tick(FPS)

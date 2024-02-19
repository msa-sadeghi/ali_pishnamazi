import random
from constants import *
from utils import *

score = 0
lives = 3
chick_rect = chick_image.get_rect()
chick_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
salad_rect = salad_image.get_rect()
salad_rect.bottom = SCREEN_HEIGHT
salad_rect.centerx = random.randint(32, SCREEN_WIDTH-32)
score_text= game_font.render(f"Score:{score}", True, (190,10,180))
score_rect = score_text.get_rect(top=0, centerx=SCREEN_WIDTH/2)
lives_text= game_font.render(f"lives:{lives}", True, (190,10,180))
lives_rect = lives_text.get_rect(topleft=(0,0))
pygame.mixer.music.load("assets/music.wav")
pygame.mixer.music.play(-1)
catch_sound = pygame.mixer.Sound("assets/coin.wav")
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
            lives,score = game_over()

        
    
    score_text= game_font.render(f"Score:{score}", True, (190,10,180))
    lives_text= game_font.render(f"lives:{lives}", True, (190,10,180))
    

    screen.fill((0,0,0))
    screen.blit(chick_image, chick_rect)
    screen.blit(salad_image, salad_rect)
    screen.blit(score_text, score_rect)
    screen.blit(lives_text, lives_rect)
    pygame.display.update()
    clock.tick(FPS)

import pygame
import random
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60
score1 = 0
score2 = 0
paddle1 = pygame.Rect(50, HEIGHT//2 - 60, 20, 120 )
paddle2 = pygame.Rect(WIDTH-70, HEIGHT//2 - 60, 20, 120 )
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30 )
ball_dx = random.choice((-1,1))
# ball_dy = random.choice((-1,1))
ball_dy = 1
font = pygame.font.SysFont("arial",22)
score1_text = font.render(f"score: {score1}", True, (255,0,0))
score2_text = font.render(f"score: {score2}", True, (0,255,0))
paddle2_direction = 1
start_movement  = False
def reset_ball_position():
    global ball_speed
    ball.x = WIDTH//2 - 15
    ball.y = HEIGHT//2 - 15
    ball_speed = 3

ball_speed = 3
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start_movement = True
                
                
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and paddle1.top >0:
        paddle1.y -= 10
        
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += 10
        
    if ball.centery > paddle2.centery + 25 and paddle2.top > 100:
        paddle2_direction = 1
    elif ball.centery < paddle2.centery - 25 and paddle2.centery < HEIGHT - 100:
        paddle2_direction = -1
    if paddle2.bottom >= HEIGHT or paddle2.top <= 0:
        paddle2_direction *= -1
    
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    if ball.right <=0  and start_movement:
        score2 += 1
        start_movement  = False
        reset_ball_position()
    if ball.left >= WIDTH and start_movement:
        score1 += 1
        start_movement  = False
        reset_ball_position()
        
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1
        ball_speed += 1
    if start_movement:
        ball.x += ball_speed * ball_dx
        ball.y += ball_speed * ball_dy
    paddle2.y += 3 * paddle2_direction
    score1_text = font.render(f"score: {score1}", True, (255,0,0))
    score2_text = font.render(f"score: {score2}", True, (0,255,0))
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), paddle1)        
    pygame.draw.rect(screen, (255,255,255), paddle2) 
    pygame.draw.ellipse(screen, (255,255,255), ball)   
    screen.blit(score1_text, (10,10))    
    screen.blit(score2_text, (WIDTH - 80,10))    
    pygame.display.update()
    CLOCK.tick(FPS)
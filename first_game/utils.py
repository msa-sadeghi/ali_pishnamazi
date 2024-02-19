from constants import *
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
    return lives,score
                    
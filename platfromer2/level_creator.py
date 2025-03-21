# اضافه کردن اسکرول

import pygame
import button
import csv
import pickle
pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300
screen = pygame.display.set_mode(
    (SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')


# define game variables
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1


pine1_img = pygame.image.load('img/Background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('img/Background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('img/Background/mountain.png').convert_alpha()
sky_img = pygame.image.load('img/Background/sky_cloud.png').convert_alpha()

GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
# create function for drawing background
def draw_bg():
    screen.fill(GREEN)
    width = sky_img.get_width()
# عدد 4 انتخابی هست یعنی چند بار تصویر تکرار شود
    for x in range(4):
        # 0.5    0.6    0.7   0.8    برای سرعت های متفاوت
        screen.blit(sky_img, ((x * width) - scroll * 0.5, 0))
        screen.blit(mountain_img, ((x * width) - scroll * 0.6,
                    SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, ((x * width) - scroll * 0.7,
                    SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, ((x * width) - scroll * 0.8,
                    SCREEN_HEIGHT - pine2_img.get_height()))
run = True
while run:
    clock.tick(FPS)
    draw_bg()
    # scroll the map
    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right == True:
        scroll += 5 * scroll_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            # اضافه کردن سرع به اسکرول
            if event.key == pygame.K_RSHIFT:
                 scroll_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            # گرفتن سرعت اسکرول
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1

    pygame.display.update()
pygame.quit()

# اضافه کردن اسکرول

import pygame
import button
import csv
import pickle
from button import Button
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

MAX_COLS = 150
ROW = 16

TILE_SIZE = SCREEN_HEIGHT // ROW

tiles_images = [
    pygame.trasform.scale(
    pygame.image.load(f'assets/images/tiles/{i}.png'), (TILE_SIZE, TILE_SIZE))
    
    for i in range(20)
]


tiles_btns = []
row_id = 0
col_id = 0
for i in range(len(tiles_images)):
    tile_btn = Button(SCREEN_WIDTH + col_id * 100, row_id * 100, tiles_images[i], 1)
    col_id += 1
    if col_id == 3:
        col_id = 0
        row_id += 1
    tiles_btns.append(tile_btn)



pine1_img = pygame.image.load('assets/images/background/pine1.png')
pine2_img = pygame.image.load('assets/images/background/pine2.png')
mountain_img = pygame.image.load('assets/images/background/mountain.png')
sky_img = pygame.image.load('assets/images/background/sky_cloud.png')

GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
# create function for drawing background
def draw_bg():
    global max_width 
    screen.fill(GREEN)
    width = sky_img.get_width()
    max_width = 4 * width
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

def draw_grid():

    for i in range(ROW + 1):
        pygame.draw.line(screen, "white", (0, i * TILE_SIZE), (SCREEN_WIDTH, i * TILE_SIZE))
    for i in range(MAX_COLS + 1):
        pygame.draw.line(screen, "white", (i * TILE_SIZE -scroll, 0), (i * TILE_SIZE -scroll, SCREEN_HEIGHT))
    


run = True
while run:
    clock.tick(FPS)
    draw_bg()
    # scroll the map
    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll < 0:
        scroll = 0
    if scroll_right == True and scroll < max_width:
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
    draw_grid()
    pygame.draw.rect(screen, "lightgreen", (SCREEN_WIDTH, 0, SIDE_MARGIN, screen.get_height()))
    pygame.display.update()
pygame.quit()

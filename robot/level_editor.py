import pygame
import button
import csv
import pickle
from button import Button
import os
pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 350

screen = pygame.display.set_mode(
    (SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')


# define game variables
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1
MAX_COLS = 150
level = 1

font = pygame.font.SysFont("arial", 15)
level_text = font.render(f"level: {level}", True, "red")

ROW = 16
current_tile = 0
TILE_SIZE = SCREEN_HEIGHT // ROW

tiles_images = [
    pygame.transform.scale(
    pygame.image.load(f'game_world/Tiles/{img}'), (TILE_SIZE, TILE_SIZE))
    
    for img in os.listdir('game_world/Tiles') 
]


tiles_btns = []
row_id = 0
col_id = 0
for i in range(len(tiles_images)):
    tile_btn = Button(SCREEN_WIDTH + col_id * 70 + 70, row_id * 70 + 40, tiles_images[i], 1)
    col_id += 1
    if col_id == 4:
        col_id = 0
        row_id += 1
    tiles_btns.append(tile_btn)

world_data = []
for row in range(ROW):
    r = []
    for col in range(MAX_COLS):
        r.append(-1)
    world_data.append(r)
def draw_world():
    for i in range(ROW):
        for j in range(MAX_COLS):
            if world_data[i][j] != -1:
                screen.blit(tiles_images[world_data[i][j]], (j * TILE_SIZE - scroll, i * TILE_SIZE))


GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
# create function for drawing background


def draw_grid():

    for i in range(ROW + 1):
        pygame.draw.line(screen, "black", (0, i * TILE_SIZE), (SCREEN_WIDTH, i * TILE_SIZE))
    for i in range(MAX_COLS + 1):
        pygame.draw.line(screen, "black", (i * TILE_SIZE -scroll, 0), (i * TILE_SIZE -scroll, SCREEN_HEIGHT))
    
load_btn_image = pygame.transform.scale_by(pygame.image.load("load.png"), 0.3)
save_btn_image = pygame.transform.scale_by(pygame.image.load("save.png"),0.3)
load_btn = Button(SCREEN_WIDTH//2 + 100, SCREEN_HEIGHT + 10, load_btn_image, 1)
save_btn = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT + 10, save_btn_image, 1)


run = True
while run:
    clock.tick(FPS)
  
    # scroll the map
    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll < 0:
        scroll = 0
    if scroll_right == True and scroll < SCREEN_WIDTH:
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
            if event.key == pygame.K_UP:
                 level += 1
            if event.key == pygame.K_DOWN:
                 level -= 1
                 if level < 1:
                     level = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            # گرفتن سرعت اسکرول
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1
            
    screen.fill("lightpink")
    draw_grid()
    mouse_pos = pygame.mouse.get_pos()
    col = (mouse_pos[0] + scroll) // TILE_SIZE
    
    row = mouse_pos[1] // TILE_SIZE
    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] < SCREEN_WIDTH and mouse_pos[1] < SCREEN_HEIGHT:
            
                world_data[row][col] = current_tile
    if pygame.mouse.get_pressed()[2]:
        world_data[row][col] = -1
    pygame.draw.rect(screen, "lightgreen", (SCREEN_WIDTH, 0, SIDE_MARGIN, screen.get_height()))
    for btn in tiles_btns:
        if btn.draw(screen):
            current_tile = tiles_btns.index(btn)
    if load_btn.draw(screen):
        pass
    if save_btn.draw(screen):
        pass       
    draw_world()
    level_text = font.render(f"level: {level}", True, "red")
    screen.blit(level_text, (SCREEN_WIDTH + 20,0))
    pygame.display.update()
pygame.quit()

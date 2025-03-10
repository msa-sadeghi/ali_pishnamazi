import pygame
from button import Button

WIDTH = 800
HEIGHT = 640
SIDE_MARGIN = 300
LOWER_MATGIN = 100
ROWS = 16
MAX_COLS = 150
TILE_SIZE = HEIGHT // ROWS
TILE_TYPES = 21
level = 0
scroll = 0
scroll_speed = 1
scroll_left, scroll_right = (False, False)

pine1_image = pygame.image.load("./assets/images/background/pine1.png")
pine2_image = pygame.image.load("./assets/images/background/pine2.png")
mountain_image = pygame.image.load("./assets/images/background/mountain.png")
sky_image = pygame.image.load("./assets/images/background/sky_cloud.png")

image_list = [
    pygame.transform.scale(
        pygame.image.load(f"./assets/images/tile/{i}.png") ,
        (TILE_SIZE, TILE_SIZE)
    )
    for i in range(21)
]
current_tile = 0
button_list = []
col = 0
row = 0
for i in range(len(image_list)):
    tile = Button(
        WIDTH + 50 + col * 75,
        50 + row * 75,
        image_list[i],
        1
    )
    button_list.append(tile)
    col += 1
    if col == 3:
        col = 0
        row += 1
    



def draw_bg():
    screen.fill("green")
    width = sky_image.get_width()
    for i in range(4):
        screen.blit(sky_image, (i * width - scroll * 0.4, 0))
        screen.blit(mountain_image, (i * width - scroll * 0.5, HEIGHT - mountain_image.get_height() - 300))
        screen.blit(pine1_image, (i * width - scroll * 0.6, HEIGHT - pine1_image.get_height() - 150))
        screen.blit(pine2_image, (i * width - scroll * 0.7, HEIGHT - pine2_image.get_height() ))

def draw_grid():
    for i in range(MAX_COLS + 1):
        pygame.draw.line(screen, "white", (i * TILE_SIZE - scroll,0), (i * TILE_SIZE - scroll,HEIGHT))
        
    for j in range(ROWS + 1):
        pygame.draw.line(screen, "white", (0, j * TILE_SIZE), (WIDTH, j * TILE_SIZE))
    


screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MATGIN))
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True  
            if event.key == pygame.K_RIGHT:
                scroll_right = True  
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False  
            if event.key == pygame.K_RIGHT:
                scroll_right = False  
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1 
    
    draw_bg()
    draw_grid()
    pygame.draw.rect(screen, "green", (WIDTH, 0, SIDE_MARGIN, HEIGHT + LOWER_MATGIN))
    for i in range(len(button_list)):
        if button_list[i].draw(screen):
            current_tile = i
    pygame.draw.rect(screen, "red", button_list[current_tile].rect, 2)        
    if scroll_left and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right:
        scroll += 5 * scroll_speed
    pygame.display.update()
    clock.tick(FPS)
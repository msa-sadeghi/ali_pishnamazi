import pygame
pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
chick_image = pygame.image.load("assets/chick.png")
salad_image = pygame.image.load("assets/salad.png")
game_font = pygame.font.Font("assets/font.otf",34)
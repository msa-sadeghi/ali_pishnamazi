import pygame
class World:
    def __init__(self, world_data):
        self.tiles = []
        self.image = pygame.image.load("assets/sky.png")
        self.image = pygame.transform.scale(self.image, (1000, 700))
        
    def draw(self, screen):
        screen.blit(self.image, (0,0))
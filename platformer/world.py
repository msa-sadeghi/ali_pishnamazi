import pygame
from blob import Blob
from hiddengrass import HiddenGrass
class World:
    def __init__(self, world_data, blob_group, hidden_grass_group):
        dirt_image = pygame.image.load("assets/dirt.png")
        grass_image = pygame.image.load("assets/grass.png")
        self.tiles = []
        self.image = pygame.image.load("assets/sky.png")
        self.image = pygame.transform.scale(self.image, (1000, 700))
        for i in range(len(world_data)):
            for j in range(len(world_data[i])):
                if world_data[i][j] == 1:
                    img = pygame.transform.scale(dirt_image,(50,50))
                    rect = img.get_rect(topleft=(j * 50, i * 50))
                    self.tiles.append((img, rect))
                if world_data[i][j] == 2:
                    img = pygame.transform.scale(grass_image,(50,50))
                    rect = img.get_rect(topleft=(j * 50, i * 50))
                    self.tiles.append((img, rect))
                if world_data[i][j] == 3:
                    Blob(j * 50, i * 50 + 15,blob_group)
                if world_data[i][j] == 9:
                    HiddenGrass(j * 50, i * 50 + 15,hidden_grass_group)
                    
        
        
    def draw(self, screen):
        screen.blit(self.image, (0,0))
        for t in self.tiles:
            screen.blit(t[0], t[1])
            
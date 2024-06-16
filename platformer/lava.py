from pygame.sprite import Sprite
import pygame

class Lava(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        img = pygame.image.load("assets/lava.png")
        self.image = pygame.transform.scale(img, (50,50))
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
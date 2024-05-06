from pygame.sprite import Sprite
import pygame

class Door(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/exit.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
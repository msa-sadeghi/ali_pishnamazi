from pygame.sprite import Sprite
import pygame
import math
class Bullet(Sprite):
    def __init__(self, x,y, group, angle):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("./assets/img/bullet.png"),(50,50))
        self.rect = self.image.get_rect(center = (x,y))
        group.add(self)
        self.angle = angle
        
        
    def update(self):
        self.rect.x += math.cos(self.angle) * 10
        self.rect.y += -math.sin(self.angle) * 10
from pygame.sprite import Sprite
import os
import pygame
class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        images_names = os.listdir('assets/img/castle')
        images = [pygame.image.load(f"assets/img/castle/{item}") for item in images_names]
        img_w = images[0].get_width()
        img_h = images[0].get_height()
        self.images = [pygame.transform.scale(item, (img_w * 0.25, img_h * 0.25)) for item in images]
        self.health = 100
        self.max_health = 100
        self.alive =True
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = (x,y))
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
        
        

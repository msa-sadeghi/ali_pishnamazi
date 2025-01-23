from pygame.sprite import Sprite
import os
import pygame
import math
from bullet import Bullet
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
        self.bullet_shooted = False
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def shoot(self, group):
        if pygame.mouse.get_pressed()[0] and not self.bullet_shooted:
            self.bullet_shooted = True
            mouse_pointer_x, mouse_pointer_y = pygame.mouse.get_pos()
            y_distance = - (mouse_pointer_y - self.rect.midleft[1])
            x_distance = mouse_pointer_x - self.rect.midleft[0]
            angle = math.atan2(y_distance, x_distance)
            Bullet(self.rect.midleft[0], 
                   self.rect.midleft[1], 
                   group,
                   angle
                   )
        if not pygame.mouse.get_pressed()[0]:
            self.bullet_shooted = False
    
        
        

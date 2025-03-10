from pygame.sprite import Sprite
import pygame


class Explosion(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.images = []
        for i in range(1, 6):
            img = pygame.image.load(f"assets/images/explosion/exp{i}.png")
            w = img.get_width()
            h = img.get_height()
            img = pygame.transform.scale(img, (w * 2, h * 2))
            self.images.append(img)
            
        self.image_number = 0
        self.image = self.images[self.image_number]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
        self.last_anim_time = 0
        
    def update(self):
        if pygame.time.get_ticks() - self.last_anim_time > 200:
            self.last_anim_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.image_number]
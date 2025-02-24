import os
from pygame.sprite import Sprite
import pygame

class Enemy(Sprite):
    def __init__(self, type, x,y, health, attack_power, injury_amount, speed):
        super().__init__()
        self.type = type
        self.health = health
        self.attack_power = attack_power
        self.injury_amount = injury_amount
        self.animation_types = os.listdir(f"assets/img/enemies/{type}")
        self.all_images = {}
        for animation in self.animation_types:
            temp = []
            num_of_images = len(os.listdir(f"assets/img/enemies/{type}/{animation}"))
            for i in range(num_of_images):
                img = pygame.image.load(f"assets/img/enemies/{type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 0.2, img_h * 0.2))
                temp.append(img)
                
            self.all_images[animation] = temp
        self.frame_index = 0
        self.action = self.animation_types[2]
        self.image = self.all_images[self.action][self.frame_index]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.last_image_change_time = 0
        self.last_move_time = 0
        self.speed = speed
        self.last_injury_time = pygame.time.get_ticks()
        
        
    def update(self, castle):
        if pygame.time.get_ticks() - self.last_move_time > 100:
            self.last_move_time = pygame.time.get_ticks()
            self.rect.x += self.speed
        self.image = self.all_images[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.last_image_change_time > 100:
            self.last_image_change_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.action]):
                self.frame_index = 0

        if self.rect.colliderect(castle.rect):
            if pygame.time.get_ticks() - self.last_injury_time > 1000:
                self.last_injury_time = pygame.time.get_ticks()
                castle.health -= self.injury_amount
                self.speed = 0
                self.action = "attack"

            

        
 
        
        


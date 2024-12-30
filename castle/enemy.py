import os
from pygame.sprite import Sprite
import pygame

class Enemy(Sprite):
    def __init__(self, type, x,y, health, attack_power, injury_amount):
        super().__init__()
        self.type = type
        self.health = health
        self.attack_power = attack_power
        self.injury_amount = injury_amount
        self.animation_types = os.listdir(f"assets/img/enemies/{type}")
        self.all_images = {}
        for animation in self.animation_types:
            temp = []
            num_f_images = len(os.listdir(f"assets/img/enemies/{type}/{animation}"))
            for i in range(num_f_images):
                img = pygame.image.load(f"assets/img/enemies/{type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
        
        


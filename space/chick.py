from pygame.sprite import Sprite
from constants import *
import random
from egg import Egg
class Chick(Sprite):
    
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)    
        self.direction = 1
        self.speed = 4 
        group.add(self)  
        
        
    def update(self, group):
        self.rect.x += self.direction * self.speed
        self.fire(group)
        
    def fire(self, group):
        if random.randint(1,1000) == 1000:
            Egg(self.rect.centerx , self.rect.bottom, group)
            
        
        
        
        
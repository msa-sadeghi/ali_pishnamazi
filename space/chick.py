from pygame.sprite import Sprite
from constants import *
class Chick(Sprite):
    
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)    
        self.direction = 1
        self.speed = 4 
        group.add(self)  
        
        
    def update(self):
        self.rect.x += self.direction * self.speed
        
        
        
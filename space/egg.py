from pygame.sprite import Sprite
from constants import *
class Egg(Sprite):
    
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/egg.png")
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        
        group.add(self)  
        
        
    def update(self):
        self.rect.y += 5
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()
        
        
        
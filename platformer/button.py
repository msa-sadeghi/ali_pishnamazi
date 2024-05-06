import pygame
class Button:
    def __init__(self, image, x,y) -> None:
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def check_click(self):
        res = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                res = True
        return res
    
    

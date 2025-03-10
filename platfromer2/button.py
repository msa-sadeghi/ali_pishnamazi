import pygame

class Button:
    def __init__(self, x,y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (scale * width, scale * height))
        self.rect = self.image.get_rect(topleft=(x,y))
        
        self.clicked = False
        
    def draw(self, screen):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True
                
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            
        screen.blit(self.image, self.rect)
        
        return action
                
                
        
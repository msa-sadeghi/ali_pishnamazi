import pygame

class MousePointer:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("./assets/img/crosshair.png"), (48,48))
        
        pygame.mouse.set_visible(False)
    def draw(self, screen):
        self.rect = self.image.get_rect(center=(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))
        screen.blit(self.image,self.rect)
        
        
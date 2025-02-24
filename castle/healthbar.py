import pygame
class HealthBar:
    def __init__(self):
        pass

    def update(self,screen, health):
        ratio = health/100 
        pygame.draw.rect(screen, "red", (10,10, 150, 20))
        pygame.draw.rect(screen, "green", (10,10, 150 * ratio, 20))
    
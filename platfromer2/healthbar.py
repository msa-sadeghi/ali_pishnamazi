import pygame
class HealthBar:
    def __init__(self, x,y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        
    def draw(self,screen, health):
        pygame.draw.rect(screen, "red", (self.x, self.y, 140, 10))
        pygame.draw.rect(screen, "green", (self.x, self.y, 140 * health/self.max_health, 10))
        
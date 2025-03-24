
from pygame.sprite import Sprite
import pygame
class Rock(Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("./Objects/rock.png")
        self.image = pygame.transform.scale_by(image, 0.2)
        self.rect = self.image.get_rect(topleft=(1100, 600 - self.image.get_height()))
        self.last_injury = False


    def update(self, player):
        self.rect.x -= 5

        if player.rect.colliderect(self.rect) and player.sliding:
            self.kill()
            player.health += 10
        elif player.rect.colliderect(self.rect) and not self.last_injury:
            player.health -= 10
            self.last_injury = True
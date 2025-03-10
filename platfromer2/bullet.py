from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, x,y, direction):
        super().__init__()
        self.speed = 6
        self.image = pygame.image.load("assets/images/icons/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        
        
        
    def update(self, player, enemy_group, player_bullet_group, enemy_bullet_group):
        self.rect.x += self.speed * self.direction
        if self.rect.right < 0 or self.rect.left > 800:
            self.kill()
        if pygame.sprite.spritecollide(player, enemy_bullet_group, False) :
            if player.alive:
                player.health -= 25
                self.kill()   
        for enemy in enemy_group.sprites():
            if pygame.sprite.spritecollide(enemy, player_bullet_group, False) :
                if enemy.alive:
                    enemy.health -= 25
                    self.kill()   
        
        
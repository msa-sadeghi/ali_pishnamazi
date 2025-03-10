from pygame.sprite import Sprite
from explosion import Explosion
import pygame


class Grenade(Sprite):
    def __init__(self, x, y, group, direction):
        super().__init__()
        self.image = pygame.image.load("assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 7
        self.vel_y = -11
        self.timer = 100
        group.add(self)
        self.bounces = 0
        self.max_bounces = 2

    def update(self, explosion_group, player, enemy_group):
        dx = self.direction * self.speed
        dy = self.vel_y

        self.vel_y += 1

        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            dx = 0
            self.vel_y = -0.7 * self.vel_y
            self.bounces += 1
        if self.bounces >= self.max_bounces and self.vel_y >= 0:
            self.vel_y = 0
            dy = 300 - self.rect.bottom
            dx = 0
        if self.rect.left + dx < 0 or self.rect.right + dx > 800:
            self.direction *= -1

        self.rect.x += dx
        self.rect.y += dy
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y)
            explosion_group.add(explosion)
            if abs(self.rect.centerx - player.rect.centerx) < 100 and \
                    abs(self.rect.centery - player.rect.centery) < 100:
                player.health -= 50
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < 100 and \
                        abs(self.rect.centery - enemy.rect.centery) < 100:
                    enemy.health -= 50
                    enemy.injury = True

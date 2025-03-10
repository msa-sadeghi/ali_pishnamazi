from pygame.sprite import Sprite
import pygame
import os
from bullet import Bullet
from grenade import Grenade
import random

class Solider(Sprite):
    def __init__(self, type, x, y, ammo, grenade):
        super().__init__()
        self.animation_types = ("Idle", "Run", "Jump", "Death")
        self.all_images = []
        for anim in self.animation_types:
            temp = []
            n = len(os.listdir(f"assets/images/{type}/{anim}"))
            for i in range(n):
                img = pygame.image.load(f"assets/images/{type}/{anim}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 2, img_h * 2))
                temp.append(img)
            self.all_images.append(temp)

        self.action = 0
        self.image_number = 0
        self.image = self.all_images[self.action][self.image_number]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 1000
        self.max_health = 1000
        self.ammo = ammo
        self.grenades = grenade
        self.last_update = 0
        self.jump = False
        self.flip = False
        self.vel_y = 0
        self.direction = 1
        self.in_air = False
        self.alive = True
        self.vision = pygame.Rect(self.rect.x, self.rect.y, 150, 20)
        self.idling = True
        self.type = type
        self.last_shoot_time = 0
        self.move_counter = 0
        self.injury = False
        self.last_injury_time = 0

    def draw(self, screen):
        self.image = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(self.image, self.rect)
        pygame.draw.line(screen, "red", (0, 300), (600, 300))

    def update(self):
        self.animation()
        self.is_alive()

    def move(self, moving_left, moving_right):

        dx = 0
        dy = 0
        if moving_left:
            dx -= 5
            self.flip = True
            self.direction = -1

        if moving_right:
            dx += 5
            self.flip = False
            self.direction = 1
        if self.jump:
            self.in_air = True
            self.vel_y = -13
        dy += self.vel_y

        self.vel_y += 1
        if self.rect.bottom + dy > 300:

            dy = 300 - self.rect.bottom

            if self.injury:
                print("++++++++++++++++")
                self.vel_y = -10
                self.injury = False
            else:
                self.vel_y = 0
            self.in_air = False

        if self.type == "enemy":
            print(dy)
        self.rect.x += dx
        self.rect.y += dy

    def animation(self):

        self.image = self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_update > 100:
            self.last_update = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                if self.action == 3:
                    self.image_number = len(self.all_images[self.action]) - 1
                else:
                    self.image_number = 0

    def set_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.image_number = 0

    def is_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.set_action(3)

    def shoot(self, type_, group):
        if type_ == "bullet":
            if self.ammo > 0 and pygame.time.get_ticks() - self.last_shoot_time > 200:
                self.last_shoot_time = pygame.time.get_ticks()
                bullet = Bullet(self.rect.centerx + self.direction * self.rect.size[0] * 0.5,
                                self.rect.centery, self.direction
                                )
                group.add(bullet)
                self.ammo -= 1
        elif type_ == "grenade":
            if self.grenades > 0:
                Grenade(self.rect.centerx + 0.5 * self.rect.size[0] * self.direction,
                        self.rect.centery, group, self.direction
                        )
                self.grenades -= 1

    def ai(self, player, bullet_group, ai_moving_left, ai_moving_right, screen):

        # pygame.draw.rect(screen, "red", self.vision, 3)

        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.set_action(0)
                self.idling = True
                self.move_counter = 50
            if self.vision.colliderect(player.rect):

                self.set_action(0)
                self.shoot("bullet", bullet_group)
                self.idling = True
            else:
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.set_action(1)
                    self.vision.center = (
                        self.rect.centerx + 120 * self.direction, self.rect.centery)
                    self.move_counter += 1
                    if self.move_counter > 50:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.move(ai_moving_left, ai_moving_right)
                    self.set_action(1)
                    self.idling = False

        return ai_moving_left, ai_moving_right

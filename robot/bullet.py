from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.all_images = []
        for i in range(5):
            img = pygame.image.load(f"./Objects/Bullet/Bullet_00{i}.png")
            img = pygame.transform.scale_by(img, 0.4)
            self.all_images.append(img)

        self.image = self.all_images[0]
        self.rect = self.image.get_rect(center=(x,y))
        self.frame_index = 0
        self.last_update_time = pygame.time.get_ticks()
        group.add(self)
        self.direction = direction

    def update(self):
        self.image = pygame.transform.flip(
            self.all_images[self.frame_index],
            True if self.direction == -1 else False,
            False
            )
        
        if pygame.time.get_ticks() - self.last_update_time >= 100:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.all_images):
                self.frame_index = 0

        self.rect.x += 5 * self.direction
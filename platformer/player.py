from pygame.sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.right_images = []
        self.left_images = []
        self.image_number = 0
        for i in range(1,5):
            img = pygame.image.load(f"assets/guy{i}.png")
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
            
        self.image = self.right_images[self.image_number]
        self.rect = self.image.get_rect(topleft=(100, 400))
        self.last_update = pygame.time.get_ticks()
        self.moving_status = False
        self.direction = 1
        
    def draw(self, screen):
        
        screen.blit(self.image, self.rect)
        self.animation()
    
    def move(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving_status = True
            self.direction = -1
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.moving_status = True
            self.direction = 1
            dx += 5
        if not  keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving_status = False  
        self.rect.x += dx
        self.rect.y += dy
    
    def animation(self):
        if pygame.time.get_ticks() - self.last_update > 100:
            self.last_update = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.right_images) or not self.moving_status:
                self.image_number = 0
        if self.direction == 1:
            self.image = self.right_images[self.image_number]
        elif self.direction == -1:
            self.image = self.left_images[self.image_number]
            
            
        
        
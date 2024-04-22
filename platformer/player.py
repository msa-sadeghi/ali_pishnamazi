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
        self.yvel = 0
        self.jumped = False
        
    def draw(self, screen):
        
        screen.blit(self.image, self.rect)
        self.animation()
    
    def move(self, tiles, blob_group):
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
        if keys[pygame.K_SPACE] and not self.jumped:
            self.yvel = -17
            self.jumped = True
        dy += self.yvel
        self.yvel += 1
        
        for t in tiles:
            if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                if self.yvel > 0:
                    dy = t[1].top - self.rect.bottom
                    self.jumped = False
                else:
                    
                    dy = t[1].bottom - self.rect.top
                self.yvel = 0
            if t[1].colliderect(self.rect.x + dx, self.rect.y , self.rect.size[0], self.rect.size[1]):
                dx =0
        
        
        for blob in blob_group:
            if blob.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.size[0], self.rect.size[1]):
                if self.yvel > 1:
                    print(self.yvel)
                    blob.kill()
                else:
                    print("die!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
        
        
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
            
            
        
        
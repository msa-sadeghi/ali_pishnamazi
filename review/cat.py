import pygame
class Cat:
    def __init__(self, screen_width : int, screen_height : int):
        self.right_images = []
        self.left_images = []
        for i in range(2):
            image = pygame.image.load(f"cat{i + 1}.svg")
            self.right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.left_images.append(image)
        self.image = self.right_images[0]
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height / 2))
        self.direction = 1
        self.image_number_LI = 0
        self.delay = pygame.time.get_ticks()
    def animation(self):
        keys = pygame.key.get_pressed()
        if pygame.time.get_ticks() - self.delay >= 1:
            self.delay = pygame.time.get_ticks()
            if not self.image_number_LI >= 1:
                self.image_number_LI += 1
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.image = self.right_images[self.image_number_LI]
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.image = self.left_images[self.image_number_LI]
        else:
            if self.direction == 1:
                self.image = self.right_images[0]
            if self.direction == -1:
                self.image = self.left_images[0]
    def draw(self, screen : pygame.Surface):
        screen.blit(self.image, self.rect)
        self.animation()
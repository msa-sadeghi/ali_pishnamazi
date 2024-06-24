# def my():
#     return "hii"


# assert my() == "hi"
import pygame

screen_width = 500
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
text = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
        
        
# z = "blalalall"
# y = "aaaaaaaaaaaaa"
# print(z[:-1])

# assert 1 == 12
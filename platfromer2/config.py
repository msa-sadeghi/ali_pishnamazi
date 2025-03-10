import pygame

ammo_box_image = pygame.image.load("assets/images/tile/17.png")
grenade_box_image = pygame.image.load("assets/images/tile/18.png")
health_box_image = pygame.image.load("assets/images/tile/19.png")

item_boxes = {
    'Health': health_box_image,
    'Ammo':ammo_box_image,
    'Grenade': grenade_box_image
}

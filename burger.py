import pygame

class Burger:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("burger_station.png")

        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 10, self.image_size[1] * 10)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * 10, self.image_size[1] * 10)
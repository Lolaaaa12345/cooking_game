import pygame

class Fries:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("fries_station.png")

        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 7, self.image_size[1] * 7)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * 7, self.image_size[1] * 7)
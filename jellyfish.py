import pygame

class Jellyfish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("jellyfish food")

    def enter_restaurant (self, customers, location_to_sit):
        if customers < 3
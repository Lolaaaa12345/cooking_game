import pygame
import random

class Jellyfish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("jellyfish food")

    def enter_restaurant (self, sit_x, sit_y):


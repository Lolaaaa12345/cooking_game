import pygame
import random

class Squid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("squid food.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 1

    def enter_restaurant (self, sit_x, sit_y):
        if self.x != sit_x:
            if self.x > sit_x:
                self.x = self.x - self.delta
            elif self.x < sit_x:
                self.x = self.x + self.delta
        if self.y != sit_y:
            if self.y > sit_y:
                self.y = self.y - self.delta
            if self.y < sit_y:
                self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def get_food(self, has_soda, has_burger, money_class, complete):
        if has_soda and has_burger:
            money_class += 10
            complete = True
            return money_class, complete

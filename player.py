import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Chef real.png")
        self.delta = 2

    def move_character(self, direction) :
        if direction == "up":
            if 0 <= self.y <= 550:
                self.y = self.y - self.delta
            else:
                self.y = self.y
        if direction == "down":
            if 0 <= self.y <= 550:
                self.y = self.y + self.delta
            else:
                self.y = self.y
        if direction == "left":
            if 0 <= self.x <= 750:
                self.x = self.x - self.delta
            else:
                self.x = self.x
        if direction == "right":
            if 0 <= self.x <= 750:
                self.x = self.x + self.delta
            else:
                self.x = self.x
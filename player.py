import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Chef real.png")

        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * .5, self.image_size[1] * .5)

        self.delta = 2

    def move_direction(self, direction):
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
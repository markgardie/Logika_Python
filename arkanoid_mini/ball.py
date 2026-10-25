import pygame as pg
from random import randint

class Ball():

    def __init__(self, coords, radius, speed, color):
        self.rect = pg.Rect(coords[0], coords[1], self.radius * 2, self.radius * 2)
        self.radius = radius
        self.dir_x = 1
        self.dir_y = -1
        self.speed = speed
        self.color = color

    def update(self):
        self.rect.x += self.speed * self.dir_x
        self.rect.y += self.speed * self.dir_y
        if self.rect.x > 1000 - self.radius or self.rect.x < 0:
            self.dir_x *= -1
            self.dir_y = randint(-1, 1)

        if self.rect.y < 0:
            self.dir_y *= -1
            self.dir_x = randint(-1, 1)

    def draw(self, surface):
        pg.draw.circle(surface,
                       self.color,
                       (self.rect.x + self.radius, 
                        self.rect.y + self.radius),
                        self.radius
                       )
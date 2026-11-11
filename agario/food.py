# food.py

from sprite import Sprite
from random import randint
from constants import WORLD_MIN, WORLD_MAX, FOOD_RADIUS


class Food(Sprite):
    
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, radius, color)
    
    @staticmethod
    def generate_random():
        """Генерує випадкову їжу"""
        x = randint(WORLD_MIN, WORLD_MAX)
        y = randint(WORLD_MIN, WORLD_MAX)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        return Food(x, y, FOOD_RADIUS, color)
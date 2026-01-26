
from sprite import Sprite
from pygame.key import get_pressed
from constants import PLAYER_SPEED, PLAYER_COLOR_SELF, PLAYER_COLOR_OTHER


class Player(Sprite):
    
    def __init__(self, player_id, x, y, radius, is_self=False):
        color = PLAYER_COLOR_SELF if is_self else PLAYER_COLOR_OTHER
        super().__init__(x, y, radius, color)
        self.id = player_id
        self.is_self = is_self
    
    def controls(self, key_up, key_down, key_left, key_right):
        """Управління гравцем за допомогою клавіш"""
        if not self.is_self:
            return
        
        keys = get_pressed()
        
        if keys[key_up]:
            self.y -= PLAYER_SPEED
        if keys[key_down]:
            self.y += PLAYER_SPEED
        if keys[key_left]:
            self.x -= PLAYER_SPEED
        if keys[key_right]:
            self.x += PLAYER_SPEED
    
    def update_from_data(self, x, y, radius):
        """Оновлює дані гравця з сервера"""
        self.x = x
        self.y = y
        self.radius = radius
    
    def get_data_string(self):
        """Повертає дані гравця у вигляді рядка для відправки на сервер"""
        return f"{self.id},{self.x},{self.y},{self.radius}"
    
    def grow(self, amount):
        """Збільшує розмір гравця"""
        self.radius += amount
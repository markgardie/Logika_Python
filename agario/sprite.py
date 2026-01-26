from pygame.draw import circle
from math import hypot


class Sprite:
    
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self, surface, camera_x, camera_y, scale):
        """Малює об'єкт з урахуванням позиції камери та масштабу"""
        screen_x = int((self.x - camera_x) * scale + surface.get_width() // 2)
        screen_y = int((self.y - camera_y) * scale + surface.get_height() // 2)
        scaled_radius = int(self.radius * scale)
        
        if scaled_radius > 0:
            circle(surface, self.color, (screen_x, screen_y), scaled_radius)
    
    def check_collision(self, other_x, other_y, other_radius):
        """Перевіряє колізію з іншим об'єктом"""
        dx = self.x - other_x
        dy = self.y - other_y
        distance = hypot(dx, dy)
        return distance <= self.radius + other_radius
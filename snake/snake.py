import pyglet
from collections import deque

class Snake:
    def __init__(self, start_x, start_y, cell_size):
        # Розмір клітинки
        self.cell_size = cell_size
        
        # Початкова позиція та напрям руху
        self.direction = (1, 0)  # Рух вправо за замовчуванням
        self.next_direction = (1, 0)
        
        # Тіло змійки (deque для ефективного додавання/видалення з обох кінців)
        self.body = deque([(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)])
        
        # Колір змійки
        self.color = (0, 255, 0)  # Зелений
        self.head_color = (0, 200, 0)  # Темно-зелений для голови
    
    def get_head_position(self):
       return self.body[0]
    
    def get_body_positions(self):
        return list(self.body)
    
    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.next_direction = (dx, dy)
    
    def move(self):
        pass
    
    def grow(self):
        pass
    
    def check_self_collision(self):
        pass
    
    def teleport_to(self, x, y):
        pass
    
    def draw(self):
        pass
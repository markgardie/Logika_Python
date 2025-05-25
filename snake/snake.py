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
        self.direction = self.next_direction

        head_x, head_y = self.body[0]
        new_head_pos = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.appendleft(new_head_pos)
        self.body.pop()
    
    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)
    
    def check_self_collision(self):
        head = self.body[0]
        return head in self.body[1:]
    
    def teleport_to(self, x, y):
        pass
    
    def draw(self):
        for i, (x, y) in enumerate(self.body):
            if i == 0:
                color = self.head_color
            else:
                color = self.color

            x_pixel = x * self.cell_size
            y_pixel = y * self.cell_size

            segment = pyglet.shapes.Rectangle(
                x_pixel + 1, y_pixel + 1,
                self.cell_size - 2, self.cell_size - 2,
                color = color
            )

            segment.draw()

            if i == 0:
                # Визначаємо позицію очей залежно від напрямку руху
                if self.direction == (1, 0):  # вправо
                    eye1 = pyglet.shapes.Circle(x_pixel + self.cell_size - 6, y_pixel + self.cell_size - 7, 2, color=(0, 0, 0))
                    eye2 = pyglet.shapes.Circle(x_pixel + self.cell_size - 6, y_pixel + 7, 2, color=(0, 0, 0))
                elif self.direction == (-1, 0):  # вліво
                    eye1 = pyglet.shapes.Circle(x_pixel + 6, y_pixel + self.cell_size - 7, 2, color=(0, 0, 0))
                    eye2 = pyglet.shapes.Circle(x_pixel + 6, y_pixel + 7, 2, color=(0, 0, 0))
                elif self.direction == (0, 1):  # вгору
                    eye1 = pyglet.shapes.Circle(x_pixel + 7, y_pixel + self.cell_size - 6, 2, color=(0, 0, 0))
                    eye2 = pyglet.shapes.Circle(x_pixel + self.cell_size - 7, y_pixel + self.cell_size - 6, 2, color=(0, 0, 0))
                else:  # вниз
                    eye1 = pyglet.shapes.Circle(x_pixel + 7, y_pixel + 6, 2, color=(0, 0, 0))
                    eye2 = pyglet.shapes.Circle(x_pixel + self.cell_size - 7, y_pixel + 6, 2, color=(0, 0, 0))
                
                eye1.draw()
                eye2.draw()
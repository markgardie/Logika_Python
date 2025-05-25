import pyglet
import random

class Food:
    def __init__(self, grid_width, grid_height, cell_size):
        # Параметри поля
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size
        
        # Позиція їжі (спочатку не визначена)
        self.position = (-1, -1)
        
        # Колір їжі
        self.color = (255, 0, 0)  # Червоний
    
    def spawn(self, occupied_positions):
        all_positions = [(x,y) for x in range(self.grid_width) for y in range(self.grid_height)]
        available_positions = [pos for pos in all_positions if pos not in occupied_positions]

        if available_positions:
            self.position = random.choice(available_positions)
        else:
            self.position = (-1, -1)

    
    def is_collision(self, x, y):
        """Перевіряє, чи зіткнулась змійка з їжею"""
        return (x, y) == self.position
    
    def draw(self):
        """Відображає їжу на екрані"""
        if self.position != (-1, -1):  # Перевіряємо, що їжа існує
            x, y = self.position
            x_pixel = x * self.cell_size
            y_pixel = y * self.cell_size
            
            # Малюємо круг для їжі
            food_circle = pyglet.shapes.Circle(
                x_pixel + self.cell_size // 2, 
                y_pixel + self.cell_size // 2, 
                self.cell_size // 2 - 2, 
                color=self.color
            )
            food_circle.draw()
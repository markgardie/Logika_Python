import pyglet

class GameGrid:
    def __init__(self, width, height, cell_size):
        # Розміри сітки в клітинках
        self.width = width
        self.height = height
        self.cell_size = cell_size
        
        # Колір сітки
        self.grid_color = (50, 50, 50)  # Темно-сірий
        self.background_color = (20, 20, 20)  # Майже чорний
        
        # Товщина ліній сітки
        self.line_width = 1
        
        # Чи відображати сітку
        self.show_grid = True
        
        # Створюємо фоновий прямокутник
        self.background = pyglet.shapes.Rectangle(
            0, 0,
            width * cell_size, height * cell_size,
            color=self.background_color
        )
    
    def toggle_grid(self):
        self.show_grid = not self.show_grid

    def draw(self):
        self.background.draw()

        if not self.show_grid:
            return
        
        # horizontal
        for y in range(self.height + 1):
            y_pos = y * self.cell_size
            line = pyglet.shapes.Line(
                0, y_pos,
                self.width * self.cell_size, y_pos,
                width=self.line_width,
                color = self.grid_color
            )
            line.draw()

        # vertical
        for x in range(self.width + 1):
            x_pos = x * self.cell_size
            line = pyglet.shapes.Line(
                0, x_pos,
                self.height * self.cell_size, x_pos,
                width=self.line_width,
                color = self.grid_color
            )
            line.draw()
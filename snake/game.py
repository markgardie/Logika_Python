"""
Головний клас гри, який керує всіма ігровими об'єктами та ігровим циклом
"""

import pyglet
from pyglet.window import key
from snake import Snake
from food import Food
from wall import Wall
from teleport import Teleport
from power_food import PowerFood
from game_grid import GameGrid
from game_state import GameState

class Game(pyglet.window.Window):
    def __init__(self, width, height, caption):
        super().__init__(width, height, caption=caption)
        
        self.cell_size = 20
        self.grid_width = width // self.cell_size
        self.grid_height = height // self.cell_size

        self.grid = GameGrid(self.grid_width, self.grid_height, self.cell_size)

        self.score_label = pyglet.text.Label(
            "Рахунок: 0",
            font_name="Arial",
            font_size=14,
            x=10, y = height - 25,
            anchor_x='left', anchor_y='center'
        )

    
    def _load_sounds(self):
        pass
    
    def _initialize_walls(self):
        pass
    
    def _initialize_teleports(self):
        pass
    
    def on_key_press(self, symbol, modifiers):

        if self.state.is_playing():
            if symbol == key.UP and self.snake.direction != (0, -1):
                self.snake.change_direction(0, 1)
            if symbol == key.DOWN and self.snake.direction != (0, 1):
                self.snake.change_direction(0, -1)
        
        if symbol == key.R:
            self.reset_game()

        if symbol == key.ESCAPE:
            pyglet.app.exit()

    def reset_game(self):
        pass
    
    def update(self, dt):
        pass
    
    def on_draw(self):
        pass
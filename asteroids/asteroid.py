import pyglet
import random
from . import resources
from . import util

def create_asteroids(num_asteroids, player_position):
    """Generate asteroid objects with random positions and velocities, 
    not close to the player"""
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y, _ = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image,
                                            x=asteroid_x, y=asteroid_y)
        new_asteroid.rotation = random.randint(0, 360)
        asteroids.append(new_asteroid)
    return asteroids
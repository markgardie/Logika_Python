import math
from pyglet.window import key
from . import physicalobject, resources


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        # Set some easy-to-tweak constants
        self.thrust = 300.0
        self.rotate_speed = 200.0

        self.keys = dict(left=False, right=False, up=False)

    def on_key_press(self, symbol):
        if symbol == key.W:
            self.keys["up"] = True
        if symbol == key.A:
            self.keys["left"] = True
        if symbol == key.D:
            self.keys["right"] = True

    def update(self, dt):
        # Do all the normal physics stuff
        super(Player, self).update(dt)

        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        if self.keys['right']:
            self.rotation += self.rotate_speed * dt

        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y

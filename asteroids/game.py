import pyglet
from asteroid import create_asteroids

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CAPTION = "Asteroids"
SCORES_LABEL_X = 10
SCORES_LABEL_Y = 575
SCORES_LABEL = "Score: 0"
PLAYER_X = 400
PLAYER_Y = 300
ASTEROID_NUM = 2

class Game():

    

    def create_objects(self):

        self.main_batch = pyglet.graphics.Batch()

        self.window = pyglet.window.Window(width = WINDOW_WIDTH, 
                                           height = WINDOW_HEIGHT, 
                                           caption = CAPTION)
        
        self.scores_label = pyglet.text.Label(text= SCORES_LABEL,
                                            x= SCORES_LABEL_X,
                                            y= SCORES_LABEL_Y, 
                                            batch = self.main_batch)
        
        self.player = pyglet.sprite.Sprite(img = resources.player_image,
                                      x = PLAYER_X,
                                      y = PLAYER_Y)
        
        self.asteroids = create_asteroids(ASTEROID_NUM, self.player.position)

        self.game_objects = [self.player] + self.asteroids

    @window.event
    def draw_objects(self):
        self.window.clear()

        for asteroid in self.asteroids:
            asteroid.draw()

        self.player.draw()
        self.scores_label.draw()

    def move_objects(self, dt):
        for obj in game_objects:
            obj.update(dt)
        
        self.collisions()

    def collisions(self):

        # To avoid handling collisions twice, we employ nested loops of ranges.
        # This method also avoids the problem of colliding an object with itself.
        for i in range(len(game_objects)):
            for j in range(i + 1, len(game_objects)):

                obj_1 = game_objects[i]
                obj_2 = game_objects[j]

                # Make sure the objects haven't already been killed
                if not obj_1.dead and not obj_2.dead:
                    if obj_1.collides_with(obj_2):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)

        # Get rid of dead objects

        for to_remove in [obj for obj in game_objects if obj.dead]:
            # Remove the object from any batches it is a member of
            to_remove.delete()

            # Remove the object from our list
            game_objects.remove(to_remove)

    def game_loop(self):
        self.create_objects()
        pyglet.clock.schedule_interval(self.move_objects, 1 / 120.0)
        pyglet.app.run()

Game().game_loop()
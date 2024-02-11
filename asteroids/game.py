import pyglet
from game import load, resources
from asteroid import create_asteroids

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CAPTION = "Asteroids"
SCORES_LABEL_X = 10
SCORES_LABEL_Y = 575
SCORES_LABEL = "Score: 0"
PLAYER_X = 400
PLAYER_Y = 300
ASTEROIDS_NUM = 3

class Game():

    def create_objects(self):
        self.window = pyglet.window.Window(width = WINDOW_WIDTH, 
                                           height = WINDOW_HEIGHT, 
                                           caption = CAPTION)
        
        self.scores_label = pyglet.text.Label(text= SCORES_LABEL,
                                            x= SCORES_LABEL_X,
                                            y= SCORES_LABEL_Y)
        
        self.player = pyglet.sprite.Sprite(img = resources.player_image,
                                      x = PLAYER_X,
                                      y = PLAYER_Y)
        
        self.asteroids = create_asteroids(ASTEROIDS_NUM, self.player.position)

        self.game_objects = [self.player] + self.asteroids

    @self.window.event
    def draw_objects(self):
        self.scores_label.draw()
        self.player.draw()

    def move_objects(self, dt):
        for obj in self.game_objects:
            obj.update(dt)

    def collisions(self):
        for i in range(len(game_objects)):
            for j in range(i + 1, len(game_objects)):

                obj_1 = game_objects[i]
                obj_2 = game_objects[j]

                if not obj_1.dead and not obj_2.dead:
                    obj_1.collide(obj_2)
                    
        for to_remove in [obj for obj in game_objects if obj.dead]:
            to_remove.delete()
            game_objects.remove(to_remove)

    def game_loop(self):
        self.create_objects()
        pyglet.app.run()

Game().game_loop()
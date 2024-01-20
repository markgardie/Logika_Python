import pyglet
from game import load, resources

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CAPTION = "Asteroids"
SCORES_LABEL_X = 10
SCORES_LABEL_Y = 575
SCORES_LABEL = "Score: 0"
PLAYER_X = 400
PLAYER_Y = 300

class Game():

    def create_objects(self):
        self.window = pyglet.window.Window(width = WINDOW_WIDTH, 
                                           height = WINDOW_HEIGHT, 
                                           caption = CAPTION)
        
        self.scores_label = pyglet.text.Label(text= SCORES_LABEL,
                                            x= SCORES_LABEL_X,
                                            y= SCORES_LABEL_Y)
        
        player = pyglet.sprite.Sprite(img = resources.player_image,
                                      x = PLAYER_X,
                                      y = PLAYER_Y)
        
    def create_asteroids(self):
        pass

    def draw_objects(self):
        pass

    def game_loop(self):
        self.create_objects()
        pyglet.app.run()

Game().game_loop()
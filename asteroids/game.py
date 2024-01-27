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
        self.window = pyglet.window.Window(width = WINDOW_WIDTH, 
                                           height = WINDOW_HEIGHT, 
                                           caption = CAPTION)
        
        self.scores_label = pyglet.text.Label(text= SCORES_LABEL,
                                            x= SCORES_LABEL_X,
                                            y= SCORES_LABEL_Y)
        
        self.player = pyglet.sprite.Sprite(img = resources.player_image,
                                      x = PLAYER_X,
                                      y = PLAYER_Y)
        
        self.asteroids = create_asteroids(ASTEROID_NUM, self.player.position)
    @window.event
    def draw_objects(self):
        self.window.clear()

        for asteroid in self.asteroids:
            asteroid.draw()

        self.player.draw()
        self.scores_label.draw()

    def game_loop(self):
        self.create_objects()
        pyglet.app.run()

Game().game_loop()
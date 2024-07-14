from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__()

        self.model = loader.load('models/environment')
        self.model.reparentTo(render)
        self.model.setPos(-2, 25, -3)
        self.model.setScale(0.1)


game = Game()
game.run()
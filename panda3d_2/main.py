from direct.showbase.ShowBase import ShowBase, Loader
from mapmanager import MapManager

class Game(ShowBase):

    def __init__(self):
        ShowBase.__init_(self)

        self.manager = MapManager()
        base.camLens.setPov(90)


Game.run()
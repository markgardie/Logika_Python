from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager

class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.manager = MapManager()
        base.camLens.setPov(90)


Game().run()
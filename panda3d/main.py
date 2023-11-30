
from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager

class Game(ShowBase):
      def __init__(self):
        ShowBase.__init__(self)
        self.land = MapManager()
        self.land.loadLand('land3.txt')  # створюємо карту
        base.camLens.setFov(90)

Game().run()

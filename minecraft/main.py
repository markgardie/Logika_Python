
from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

LAND_PATH = r"minecraft-final\land.txt"

class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.land = MapManager()
        width, height = self.land.loadLand(LAND_PATH)
        self.hero = Hero((width // 2, height // 2, 2), self.land)
        base.camLens.setFov(90)


class Game(ShowBase):
      def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()   # створюємо карту
        base.camLens.setFov(90)

Game.run()

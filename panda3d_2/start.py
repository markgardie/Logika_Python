from direct.showbase.ShowBase import ShowBase


class Game(ShowBase):

    def __init__(self):
        ShowBase.__init_(self)

        model = loader.loadModel('models/environment')
        model.reparentTo(render)
        model.setScale(0.1)
        model.setPos(-2, 25, -3)


Game().run()

        


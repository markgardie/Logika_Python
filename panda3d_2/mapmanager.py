from direct.showbase.ShowBase import ShowBase, Loader

class MapManager():

    def __init__(self):
        
        self.model = 'block.egg'
        self.texture = 'block.png'

        self.color = (0.2, 0.2, 0.35, 1)

        self.startNew()
        self.addBlock((0,10, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def 
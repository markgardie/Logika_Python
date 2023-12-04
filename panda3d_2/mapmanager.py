from direct.showbase.ShowBase import ShowBase

class MapManager():

    def __init__(self):
        
        self.model = 'block.egg'
        self.texture = 'block.png'

        self.colors = [
           (0.2, 0.2, 0.35, 1),
           (0.2, 0.5, 0.2, 1),
           (0.7, 0.2, 0.2, 1),
           (0.5, 0.3, 0.0, 1)
       ]

        self.startNew()
        self.addBlock((0,10, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")
        
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)

        self.color = self.getColor(int(position[2]))

        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]
        
    def loadLand(self, path):
        self.clear()

        with open(path) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for place in line:
                    for z in range(int(place) + 1):
                        self.addBlock((x, y, z))
                    x += 1
                y += 1

    def clear(self):
        self.land.removeNode()
        self.startNew()
                


    

    
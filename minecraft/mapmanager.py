from direct.showbase.ShowBase import ShowBase
import pickle

class MapManager():
    def __init__(self):
       pass

    def startNew(self):
        self.land = render.attachNewNode("Land")
  
    def getColor(self, z):
        if z < len(self.colors):
           return self.colors[z]
        else:
           return self.colors[len(self.colors) - 1]

    
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def loadLand(self, filename):
       pass

    def clear(self):
       pass

    def findBlocks(self, pos):
       pass


    def isEmpty(self, pos):
       pass


    def findHighestEmpty(self, pos):
       pass


    def buildBlock(self, pos):
       pass


    def delBlock(self, position):
       pass


    def delBlockFrom(self, position):
       pass

    def saveMap(self):
       pass


    def loadMap(self):
       pass
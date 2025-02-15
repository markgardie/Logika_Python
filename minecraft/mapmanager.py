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
      self.clear()
      with open(filename) as file:
         y = 0
         for row in file:
            x = 0
            row = row.split(" ")
            for cell in row:
               for height in range(int(cell) + 1):
                  block = self.addBlock((x, y, height))
               x += 1
            y += 1

      return x, y

   def clear(self):
      self.land.removeNode()
      self.startNew()

   def findBlocks(self, pos):
      return self.land.findAllMatches("=at=" + str(pos))


   def isEmpty(self, pos):
       blocks = self.findBlocks(pos)
       if blocks:
           return False
       else:
           return True


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
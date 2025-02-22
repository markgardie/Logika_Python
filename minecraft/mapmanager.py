from direct.showbase.ShowBase import ShowBase
import pickle

class MapManager():
   def __init__(self):
      self.model = 'block.egg' # модель кубика лежить у файлі block.egg
       # # використовуються такі текстури:
      self.texture = 'block.png'        
      self.colors = [
           (0.2, 0.2, 0.35, 1),
           (0.2, 0.5, 0.2, 1),
           (0.7, 0.2, 0.2, 1),
           (0.5, 0.3, 0.0, 1)
      ] #rgba

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
       x, y, z = pos
       z = 1
       while not self.isEmpty((x, y, z)):
           z += 1
       return (x, y, z)


   def buildBlock(self, pos):
       """Ставимо блок з урахуванням гравітації: """
       x, y, z = pos
       new = self.findHighestEmpty(pos)
       if new[2] <= z + 1:
           self.addBlock(new)


   def delBlock(self, position):
       """видаляє блоки у зазначеній позиції """
       blocks = self.findBlocks(position)
       for block in blocks:
           block.removeNode()


   def delBlockFrom(self, position):
       pass

   def saveMap(self):
      blocks = self.land.getChildren()
      with open('my_map.dat', 'wb') as file:
         pickle.dump(len(blocks), file)

         for block in blocks:
            x, y, z = block.getPos()
            pos = (int(x), int(y), int(z))
            pickle.dump(pos, file)
            


   def loadMap(self):
       pass
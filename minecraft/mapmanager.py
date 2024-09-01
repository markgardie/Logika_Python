class Mapmanager():
   
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.color = (0.2, 0.2, 0.35, 1)

        self.startNew()
        self.addBlock((0, 10, 0))


    def startNew(self):
        self.land = render.attachNewNode("Land")
  
    def addBlock(self, position):
        self.block = loader.load(self.model)
        self.block.setTexture(self.texture)
        self.block.setColor(self.color)
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        
    def clear(self):
        self.land.removeNode()
        self.startNew()
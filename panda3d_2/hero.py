from direct.showbase.ShowBase import ShowBase

KEY_SWITCH_CAMERA = 'c' # камера прив'язана до героя чи ні
KEY_SWITCH_MODE = 'z' # можна проходити крізь перешкоди чи ні


KEY_FORWARD = 'w'   # крок вперед (куди дивиться камера)
KEY_BACK = 's'      # крок назад
KEY_LEFT = 'a'      # крок вліво (вбік від камери)
KEY_RIGHT = 'd'     # крок вправо
KEY_UP = 'e'      # крок вгору
KEY_DOWN = 'q'     #крок вниз


KEY_TURN_LEFT = 'n'     # поворот камери праворуч (а світу - ліворуч)
KEY_TURN_RIGHT = 'm'    # поворот камери ліворуч (а світу – праворуч)

KEY_BUILD = 'b'     # побудувати блок перед собою
KEY_DESTROY = 'v'

HERO_COLOR = (1, 0.5, 0)
SCALE = 0.3
HEADING = 180

CAMERA_POS = (0, 0, 1.5)

MODEL_PATH = 'smiley'

class Hero():

    def __init__(self, pos, land):
        self.land = land

        self.model = loader.loadModel(MODEL_PATH)
        self.model.setColor(HERO_COLOR)
        self.model.setScale(SCALE)
        self.model.setH(HEADING)
        self.model.setPos(pos)
        self.model.reparentTo(render)
        self.cameraBind()
        self.eventsHandler()

        self.mode = True 

    def cameraBind(self):
        base.disableMouse()
        base.camera.setPos(CAMERA_POS)
        base.camera.reparentTo(self.model)
        self.isCameraBind = True

    def cameraUp(self):
        base.enableMouse()
        pos = self.model.getPos()
        base.camera.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        self.isCameraBind = False

    def changeCamera(self):
        if self.isCameraBind:
            self.cameraUp()
        else:
            self.cameraBind()

    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def moveTo(self, angle):
        if self.mode:
            self.justMove(angle)
        else:
            self.tryMove(angle)

    def justMove(self, angle):
        pos = self.lookAt(angle)
        self.model.setPos(pos)


    def tryMove(self, angle):
        pos = self.lookAt(angle)

        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.model.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.model.setPos(pos)

    def lookAt(self, angle):

        x_from = round(self.model.getX())
        y_from = round(self.model.getY())
        z_from = round(self.model.getZ())

        dx, dy = self.checkDir(angle)

        x_to = x_from + dx
        y_to = y_from + dy

        return x_to, y_to, z_from
    
    def checkDir(self,angle):
       ''' повертає заокруглені зміни координат X, Y,
       відповідні переміщенню у бік кута angle.
       Координата Y зменшується, якщо персонаж дивиться на кут 0,
       та збільшується, якщо дивиться на кут 180.
       Координата X збільшується, якщо персонаж дивиться на кут 90,
       та зменшується, якщо дивиться на кут 270.
           кут 0 (від 0 до 20) -> Y - 1
           кут 45 (від 25 до 65) -> X + 1, Y - 1
           кут 90 (від 70 до 110) -> X + 1
           від 115 до 155 -> X + 1, Y + 1
           від 160 до 200 -> Y + 1
           від 205 до 245 -> X - 1, Y + 1
           від 250 до 290 -> X - 1
           від 290 до 335 -> X - 1, Y - 1
           від 340 -> Y - 1
 '''
       if angle >= 0 and angle <= 20:
           return (0, -1)
       elif angle <= 65:
           return (1, -1)
       elif angle <= 110:
           return (1, 0)
       elif angle <= 155:
           return (1, 1)
       elif angle <= 200:
           return (0, 1)
       elif angle <= 245:
           return (-1, 1)
       elif angle <= 290:
           return (-1, 0)
       elif angle <= 335:
           return (-1, -1)
       else:
           return (0, -1)


    def left(self):
       angle = (self.model.getH() + 90) % 360
       self.moveTo(angle)

    def turnLeft(self):
       self.model.setH((self.model.getH() + 5) % 360)
    
    
    def build(self):
        angle = self.model.getH() % 360
        pos = self.lookAt(angle)

        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)
    
    
    def eventsHandler(self):
        base.accept(KEY_LEFT, self.left)
        base.accept(KEY_LEFT + '-repeat', self.left)

        base.accept(KEY_TURN_LEFT, self.turnLeft)
        base.accept(KEY_TURN_LEFT + '-repeat', self.turnLeft)
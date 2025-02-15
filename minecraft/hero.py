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

KEY_SAVEMAP = 'k'
KEY_LOADMAP = 'l'

class Hero():

    def __init__(self, land, pos):
        self.land = land
        self.isFreeMode = False  
        self.heroModel = loader.loadModel('smiley')
        self.heroModel.setColor(1, 0.5, 0)
        self.heroModel.setScale(SCALE)
        self.heroModel.setH(HEADING)
        self.heroModel.setPos(pos)
        self.heroModel.reparentTo(render)
        self.cameraBind()
        self.accept_events()


    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.heroModel)
        base.camera.setPos(CAMERA_POS)
        self.cameraBinded = True

    def cameraUnbind(self):
        pos = self.heroModel.getPos()
        base.mouserInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)    
        base.enableMouse()
        base.camera.reparentTo(render)
        self.cameraBinded = False

    def changeView(self):
        if self.cameraBinded:
            self.cameraUnbind()
        else:
            self.cameraBind()
    
    def move_to(self, angle):
        if self.isFreeMode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.heroModel.setPos(pos)

    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.heroModel.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.heroModel.setPos(pos)

    def look_at(self, angle):
        x_from = round(self.heroModel.getX())
        y_from = round(self.heroModel.getY())
        z_from = round(self.heroModel.getZ())

        dx, dy = self.check_dirs()

        x_to = x_from + dx
        y_to = y_from + dy

        return x_to, y_to, z_from


    def check_dirs(self,angle):
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
        
    def build(self):
        angle = self.heroModel.getH()
        pos = self.look_at(angle)
        if self.isFreeMode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        pass

    def left(self):
        angle = (self.heroModel.getH() + 90) % 360
        self.moveTo(angle)

    def turn_left(self):
        newAngle = (self.heroModel.getH() + 5) % 360
        self.heroModel.setH(newAngle)

    def up(self):
        if self.isFreeMode:
            self.heroModel.setZ(self.heroModel.getZ() + 1)
    
    def accept_events(self):
        base.accept(KEY_LEFT, self.left)
        base.accept(KEY_LEFT + '-repeat', self.left)

        base.accept(KEY_TURN_LEFT, self.turn_left)
        base.accept(KEY_TURN_LEFT + '-repeat', self.turn_left)

        base.accept(KEY_UP, self.up)
        base.accept(KEY_UP + '-repeat', self.up)
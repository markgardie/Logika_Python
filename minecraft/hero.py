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

    def __init__(self):
        pass


    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparantTo(self.heroModel)
        base.camera.setPos(CAMERA_POS)
        self.cameraBinded = True

    def cameraUnbind(self):
        pass
    
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
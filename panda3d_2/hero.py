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

    def left(self):
       angle = (self.model.getH() + 90) % 360
       self.move_to(angle)

    def turn_left(self):
       self.model.setH((self.model.getH() + 5) % 360)
    
    
    def eventsHandler(self):
        base.accept(KEY_LEFT, self.left)
        base.accept(KEY_LEFT + '-repeat', self.left)

        base.accept(KEY_TURN_LEFT, self.turn_left)
        base.accept(KEY_TURN_LEFT + '-repeat', self.turn_left)
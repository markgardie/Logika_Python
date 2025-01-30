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

    def left(self):
        angle = (self.getH() + 90) % 360
        self.moveTo(angle)

    
    def accept_events(self):
        base.accept(KEY_LEFT, left)
        base.accept(KEY_LEFT + '-repeat', left)
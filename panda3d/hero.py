from direct.showbase.ShowBase import ShowBase

KEY_SWITCH_CAMERA = 'c' # камера прив'язана до героя чи ні
KEY_SWITCH_MODE = 'z' # можна проходити крізь перешкоди чи ні


KEY_FORWARD = 'w'   # крок вперед (куди дивиться камера)
KEY_BACK = 's'      # крок назад
KEY_LEFT = 'a'      # крок вліво (вбік від камери)
KEY_RIGHT = 'd'     # крок вправо
key_up = 'e'      # крок вгору
KEY_DOWN = 'q'     #крок вниз


KEY_TURN_LEFT = 'n'     # поворот камери праворуч (а світу - ліворуч)
KEY_TURN_RIGHT = 'm'    # поворот камери ліворуч (а світу – праворуч)


class Hero():
   def __init__(self, pos, land):
       self.land = land
       self.mode = True # режим проходження крізь усе
       self.hero = loader.loadModel('smiley')
       self.hero.setColor(1, 0.5, 0)
       self.hero.setScale(0.3)
       self.hero.setPos(pos)
       self.hero.reparentTo(render)
       self.cameraBind()
       self.accept_events()


   def cameraBind(self):
       base.disableMouse()
       base.camera.setH(180)
       base.camera.reparentTo(self.hero)
       base.camera.setPos(0, 0, 1.5)
       self.cameraOn = True


   def cameraUp(self):
       pos = self.hero.getPos()
       base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
       base.camera.reparentTo(render)
       base.enableMouse()
       self.cameraOn = False




   def changeView(self):
       if self.cameraOn:
           self.cameraUp()
       else:
           self.cameraBind()


   def turn_left(self):
       self.hero.setH((self.hero.getH() + 5) % 360)


   def turn_right(self):
       self.hero.setH((self.hero.getH() - 5) % 360)


   def look_at(self, angle):
       ''' повертає координати, в які переміститься персонаж, що стоїть у точці (x, y),
        якщо він робить крок у напрямку angle'''


       x_from = round(self.hero.getX())
       y_from = round(self.hero.getY())
       z_from = round(self.hero.getZ())


       dx, dy = self.check_dir(angle)
       x_to = x_from + dx
       y_to = y_from + dy
       return x_to, y_to, z_from


   def just_move(self, angle):
       '''переміщається у потрібні координати у будь-якому випадку'''
       pos = self.look_at(angle)
       self.hero.setPos(pos)


   def move_to(self, angle):
       if self.mode:
           self.just_move(angle)
  
   def check_dir(self,angle):
       ''' повертає заокруглені зміни координат X, Y,
        відповідні переміщенню у бік кута angle.
        Координата Y зменшується, якщо персонаж дивиться на кут 0,
        та збільшується, якщо дивиться на кут 180.
        Координата X збільшується, якщо персонаж дивиться на кут 90,
        та зменшується, якщо дивиться на кут 270.  
           кут 0 (від 0 до 20)      ->        Y - 1
           кут 45 (від 25 до 65)    -> X + 1, Y - 1
           кут 90 (від 70 до 110)   -> X + 1
           від 115 до 155            -> X + 1, Y + 1
           від 160 до 200            ->        Y + 1
           від 205 до 245            -> X - 1, Y + 1
           від 250 до 290            -> X - 1
           від 290 до 335            -> X - 1, Y - 1
           від 340                   ->        Y - 1  '''
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


   def forward(self):
       angle =(self.hero.getH()) % 360
       self.move_to(angle)


   def back(self):
       angle = (self.hero.getH()+180) % 360
       self.move_to(angle)
  
   def left(self):
       angle = (self.hero.getH() + 90) % 360
       self.move_to(angle)


   def right(self):
       angle = (self.hero.getH() + 270) % 360
       self.move_to(angle)


   def accept_events(self):
       base.accept(KEY_TURN_LEFT, self.turn_left)
       base.accept(KEY_TURN_LEFT + '-repeat', self.turn_left)
       base.accept(KEY_TURN_RIGHT, self.turn_right)
       base.accept(KEY_TURN_RIGHT + '-repeat', self.turn_right)


       base.accept(KEY_FORWARD, self.forward)
       base.accept(KEY_FORWARD + '-repeat', self.forward)
       base.accept(KEY_BACK, self.back)
       base.accept(KEY_BACK + '-repeat', self.back)
       base.accept(KEY_LEFT, self.left)
       base.accept(KEY_LEFT + '-repeat', self.left)
       base.accept(KEY_RIGHT, self.right)
       base.accept(KEY_RIGHT + '-repeat', self.right)


       base.accept(KEY_SWITCH_CAMERA, self.changeView)

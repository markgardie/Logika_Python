key_switch_camera = 'c' # камера прив'язана до героя чи ні
key_switch_mode = 'z' # можна проходити крізь перешкоди чи ні


key_forward = 'w'   # крок вперед (куди дивиться камера)
key_back = 's'      # крок назад
key_left = 'a'      # крок вліво (вбік від камери)
key_right = 'd'     # крок вправо
key_up = 'e'      # крок вгору
key_down = 'q'     #крок вниз


key_turn_left = 'n'     # поворот камери праворуч (а світу - ліворуч)
key_turn_right = 'm'    # поворот камери ліворуч (а світу – праворуч)


class Hero():

    def __init__(self, pos, land):
       self.land = land
       self.mode = True # режим проходження крізь усе
       self.model = loader.loadModel('smiley')
       self.model.setColor(1, 0.5, 0)
       self.model.setScale(0.3)
       self.model.setPos(pos)
       self.model.reparentTo(render)
       self.cameraBind()
       self.accept_events()


    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.model)
        base.camera.setPos(0, 0, 1.5)
        self.cameraBinded = True

    def cameraUnbind(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraBinded = False

    def changeView(self):
       if self.cameraBinded:
           self.cameraUnbind()
       else:
           self.cameraBind()

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


    def move_up(self):
       if self.mode:
           self.hero.setZ(self.hero.getZ() + 1)

    

    def change_mode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True


    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def move_left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.model.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.model.setPos(pos)

    def accept_events(self):
        base.accept(key_left, self.move_left)
        base.accept(key_left + '-repeat', self.move_left)

    
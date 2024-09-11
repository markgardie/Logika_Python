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


    def move_left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def accept_events(self):
        base.accept(key_left, self.move_left)
        base.accept(key_left + '-repeat', self.move_left)

    
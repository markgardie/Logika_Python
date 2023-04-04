from Sprite import*
from Fireball import*
from constants import*

class Boss(Sprite):

    def generate_direction(self):

        direction_x = randint(-1, 1)
        direction_y = randint(-1, 1)

        if direction_x == 0 and direction_y == 0:
            direction_x = randint(-1, 1)
            direction_y = randint(-1, 1)

        return direction_x, direction_y

    def fire(self, fireballs):

        dir_1_x, dir_1_y = self.generate_direction()
        dir_2_x, dir_2_y = self.generate_direction()
        dir_3_x, dir_3_y = self.generate_direction()

        #TODO


        fireball1 = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT, )

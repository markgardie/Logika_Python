from Sprite import*
from Fireball import*
from constants import*


timer = 120

class Boss(Sprite):

    def generate_direction(self):

        direction_x = randint(-1, 1)
        direction_y = randint(-1, 1)

        while direction_x == 0 and direction_y == 0:
            direction_x = randint(-1, 1)
            direction_y = randint(-1, 1)

        return direction_x, direction_y

    def fire(self, fireballs):

        global timer

        if timer == 0:

            dir_1_x, dir_1_y = self.generate_direction()
            dir_2_x, dir_2_y = self.generate_direction()
            dir_3_x, dir_3_y = self.generate_direction()

            dir_xs = [dir_1_x, dir_2_x, dir_3_x]
            dir_ys = [dir_1_y, dir_2_y, dir_3_y]

            for dir_x in dir_xs:
                for dir_y in dir_ys:

                    
                    # left-top
                    if dir_x == -1 and dir_y == -1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.left, self.hitbox.top,
                                            FIREBALL_PATH, FIREBALL_SPEED)
                    
                    # left
                    if dir_x == -1 and dir_y == 0:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.left, self.hitbox.centery,
                                            FIREBALL_PATH, FIREBALL_SPEED)
                        
                    # left-bottom
                    if dir_x == -1 and dir_y == 1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.left, self.hitbox.bottom,
                                            FIREBALL_PATH, FIREBALL_SPEED)
                        
                    # top
                    if dir_x == 0 and dir_y == -1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.centerx, self.hitbox.top,
                                            FIREBALL_PATH, FIREBALL_SPEED)

                    # bottom
                    if dir_x == 0 and dir_y == 1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.centerx, self.hitbox.bottom,
                                            FIREBALL_PATH, FIREBALL_SPEED)
                        
                    # right-top
                    if dir_x == 1 and dir_y == -1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.right, self.hitbox.top,
                                            FIREBALL_PATH, FIREBALL_SPEED)
                        
                    # right
                    if dir_x == 1 and dir_y == 0:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.right, self.hitbox.centery,
                                            FIREBALL_PATH, FIREBALL_SPEED)
                    
                    # right-bottom
                    if dir_x == 1 and dir_y == 1:
                        fireball = Fireball(FIREBALL_WIDTH, FIREBALL_HEIGHT,
                                            self.hitbox.right, self.hitbox.bottom,
                                            FIREBALL_PATH, FIREBALL_SPEED)
                        
                    fireballs.append(fireball)
                    timer = 120

        else:
            timer -= 1
                    
  
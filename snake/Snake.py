from Sprite import*


class Snake(Sprite):

    def controls(self, up, down, left, right):

        key_pressed = pygame.key.get_pressed()

        if key_pressed[left]:
            self.direction_x = -1
            self.direction_y = 0
        if key_pressed[right]:
            self.direction_x = 1
            self.direction_y = 0
        if key_pressed[up]:
            self.direction_x = 0
            self.direction_y = -1
        if key_pressed[down]:
            self.direction_x = 0
            self.direction_y = 1
    
    def move(self):

        self.hitbox.x += self.speed * self.direction_x
        self.hitbox.y += self.speed * self.direction_y
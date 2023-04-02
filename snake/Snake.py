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
    
    def move(self):

        self.hitbox.x += self.speed * self.direction_x
        self.hitbox.y += self.speed * self.direction_y
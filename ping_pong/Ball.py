from Sprite import*

class Ball(Sprite):

    def move(self, direction_x, direction_y):
        self.rect.x += self.speed * direction_x
        self.rect.y += self.speed * direction_y
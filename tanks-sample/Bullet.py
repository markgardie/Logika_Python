from Sprite import*

class Bullet(Sprite):

    # рух в певному напрямку
    # тільки х, бо куля рухається тільки горизонтально 
    def move(self, direction_x):
        # напрямок може бути -1, 1
        # таким чином при множенні бути змінюватись знак швидкості
        self.hitbox.x += self.speed * direction_x
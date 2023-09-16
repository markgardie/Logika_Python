from Sprite import*

class Dino(Sprite):

    def jump(self, up, ground):
        
        keys = pg.key.get_pressed()

        if keys[up] and self.hitbox.colliderect(ground.hitbox):
            pass

    def gravity(self, ground):

        down = True

        if self.hitbox.colliderect(ground.hitbox):
            down = False

        if down:
            self.hitbox.y += GRAVITY_SPEED
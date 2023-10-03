from Sprite import*
from Constants import*

class Dino(Sprite):

    def jump(self, jump, up, down):
        
        keys = pg.key.get_pressed()

        if keys[jump] and self.hitbox.y > WINDOW_HEIGHT - 30:
            self.hitbox.y -= self.speed * JUMP_ACC

        if keys[up]:
            self.hitbox.width = DINO_WIDTH
            self.hitbox.height = DINO_HEIGHT
            self.change_image(STAND_IMAGE_PATH)

        if keys[down]:
            self.hitbox.width = DINO_HEIGHT
            self.hitbox.height = DINO_WIDTH
            self.change_image(CROUCH_IMAGE_PATH)


    def gravity(self, ground):

        down = True

        if self.hitbox.colliderect(ground.hitbox):
            down = False

        if down:
            self.hitbox.y += GRAVITY_SPEED

    def change_image(self, image_path):
        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (self.hitbox.width, self.hitbox.height))
from Sprite import*

class Dino(Sprite):

    def jump(self, up, down, jump, ground):
        
        keys = pg.key.get_pressed()

        if keys[jump] and self.hitbox.colliderect(ground.hitbox):
            self.hitbox.y -= self.speed * JUMP_ACC

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

    def change_image(self, path):
        self.image = pg.image.load(path)
        self.image = pg.transform.scale(self.image, (self.hitbox.width, self.hitbox.height))
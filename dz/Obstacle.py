class Obstacle(Sprite):
    def move(self):
        self.hitbox.x -= self.speed
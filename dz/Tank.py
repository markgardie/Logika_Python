from Sprite import*
from Constants import* 

class Tank (Sprite):
    
    def control(self, w, a, s, d):

        key_pressed = pg.key.get_pressed()

        if key_pressed [w] and self.hitbox.y > 0: 
            self.hitbox.y -= TANK_SPEED

        if key_pressed [a] and self.hitbox.x > 0:
            self.hitbox.x -= TANK_SPEED
    
        if key_pressed [s] and self.hitbox.y < WINDOW_HEIGHT:
            self.hitbox.y += TANK_SPEED
    
        if key_pressed [d] and self.hitbox.x < WINDOW_WIDTH:
            self.hitbox.x += TANK_SPEED
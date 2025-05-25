"""
Клас стану гри, який відповідає за рахунок, рівні та загальний стан гри
"""
import pyglet

class GameState:
    def __init__(self, game):
        # Посилання на основний клас гри
        self.game = game
        
        # Стан гри
        self.PLAYING = 'playing'
        self.PAUSED = 'paused'
        self.GAME_OVER = 'game_over'
        self.WIN = 'win'
        
        # Поточний стан
        self.current_state = self.PLAYING
        
        # Рахунок та рівень
        self.score = 0
        self.level = 1
        
        # Поріг для переходу на наступний рівень
        self.level_threshold = 10
        
        # Флаг невразливості (для силового бонусу)
        self.invincible = False
        self.invincible_time = 0
    
    def is_playing(self):
        """Перевіряє, чи гра в процесі"""
        return self.current_state == self.PLAYING
    
    def is_paused(self):
        """Перевіряє, чи гра на паузі"""
        return self.current_state == self.PAUSED
    
    def is_game_over(self):
        """Перевіряє, чи гра закінчена"""
        return self.current_state == self.GAME_OVER
    
    def is_win(self):
        """Перевіряє, чи гра виграна"""
        return self.current_state == self.WIN
    
    def pause(self):
        """Ставить гру на паузу"""
        if self.current_state == self.PLAYING:
            self.current_state = self.PAUSED
        elif self.current_state == self.PAUSED:
            self.current_state = self.PLAYING
    
    def game_over(self):
        """Встановлює стан 'гра закінчена'"""
        self.current_state = self.GAME_OVER
    
    def win(self):
        """Встановлює стан 'гра виграна'"""
        self.current_state = self.WIN
    
    def reset(self):
        """Скидає стан гри для нової гри"""
        self.current_state = self.PLAYING
        self.score = 0
        self.level = 1
        self.invincible = False
        self.invincible_time = 0
    
    def add_score(self, points):
        """Додає очки та перевіряє перехід на наступний рівень"""
        self.score += points
        
        # Перевіряємо досягнення порогу для нового рівня
        if self.score >= self.level * self.level_threshold:
            self.level_up()
    
    def level_up(self):
        """Підвищує рівень гри та оновлює швидкість"""
        self.level += 1
        
        # Збільшуємо швидкість змійки з кожним рівнем
        if self.level <= 10:  # Обмежуємо максимальну швидкість
            # Оновлюємо швидкість гри
            new_speed = max(0.05, self.game.snake_speed * 0.9)
            self.game.snake_speed = new_speed
            
            # Перезапускаємо таймер з новою швидкістю
            pyglet.clock.unschedule(self.game.update)
            pyglet.clock.schedule_interval(self.game.update, new_speed)
    
    def get_score(self):
        """Повертає поточний рахунок"""
        return self.score
    
    def get_level(self):
        """Повертає поточний рівень"""
        return self.level
    
    def set_invincible(self, duration):
        """Робить змійку невразливою на вказаний час"""
        self.invincible = True
        self.invincible_time = duration
    
    def update(self, dt):
        """Оновлює стан гри"""
        # Оновлюємо таймер невразливості
        if self.invincible:
            self.invincible_time -= dt
            if self.invincible_time <= 0:
                self.invincible = False
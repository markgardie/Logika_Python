
from kivy.uix.screenmanager import ScreenManager

class ExampleScreenManager(ScreenManager):
    
    def navigate_to_second(self):
        self.current = "second_screen"
        self.transition.direction = "left"

    def navigate_to_first(self):
        self.current = "first_screen"
        self.transition.direction = "left"
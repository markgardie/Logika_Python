from kivy.uix.screenmanager import ScreenManager
from screen1 import Screen1
from screen2 import Screen2

class Navigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()
        self.click_listeners()

    def create_screens(self):
        self.screen1 = Screen1(name = "screen1")
        self.screen2 = Screen2(name = "screen2")

    def add_screens(self):
        self.add_widget(self.screen1)
        self.add_widget(self.screen2)

    def click_listeners(self):
        self.screen1.next_button.on_press = self.navigate_to_second

    def navigate_to_second(self):
        self.transition.direction = "left"
        self.current = "screen2"

    def navigate_to_first(self):
        self.transition.direction = "right"
        self.current = "screen1"
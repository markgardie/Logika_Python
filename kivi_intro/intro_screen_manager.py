from kivy.uix.screenmanager import ScreenManager
from main_screen import MainScreen
from second_screen import SecondScreen


class IntroScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()
        self.click_listeners()

    def create_screens(self):
        self.main_screen = MainScreen(name = "main_screen")
        self.second_screen = SecondScreen(name = "second_screen")

    def add_screens(self):
        self.add_widget(self.main_screen)
        self.add_widget(self.second_screen)

    def click_listeners(self):
        self.main_screen.next_button.on_press = self.navigate_to_second
        self.second_screen.back_button.on_press = self.navigate_back_to_main

    def navigate_to_second(self):
        self.transition.direction = "left"
        self.current = "second_screen"

    def navigate_back_to_main(self):
        self.transition.direction = "right"
        self.current = "main_screen"

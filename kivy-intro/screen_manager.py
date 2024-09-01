from kivy.uix.screenmanager import ScreenManager
from first_screen import FirstScreen
from second_screen import SecondScreen


class IntroScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()
        self.click_listeners()

    def create_screens(self):
        self.first_screen = FirstScreen(name = "first_screen")

    def add_screens(self):
        self.add_widget(self.first_screen)

    def click_listeners(self):
        self.first_screen.next_btn.on_press = self.navigate_to_second

    def navigate_to_second(self):
        self.current = "second_screen"
        self.transition.direction = "left"

    def navigate_back_to_main(self):
        pass

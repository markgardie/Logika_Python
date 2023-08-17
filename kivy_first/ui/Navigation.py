from kivy.uix.screenmanager import ScreenManager
from ui.MainScreen import MainScreen
from ui.TextInputScreen import TextInputScreen


class Navigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()
        self.click_listeners()

    def create_screens(self):
        self.main_screen = MainScreen(name = "main")
        self.text_input_screen = TextInputScreen(name = "text_input")

    def add_screens(self):
        self.add_widget(self.main_screen)
        self.add_widget(self.text_input_screen)

    def click_listeners(self):
        self.main_screen.btn1.on_press = self.navigate_to_text_input
        self.text_input_screen.back_button.on_press = self.navigate_to_main
    
    def navigate_to_text_input(self):
        self.transition.direction = "left"
        self.current = "text_input"

    def navigate_to_main(self):
        self.transition.direction = "right"
        self.current = "main"
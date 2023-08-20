from kivy.uix.screenmanager import ScreenManager
from ui.MainScreen import MainScreen
from ui.PasswordScreen import PasswordScreen

class Navigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()
        self.click_listeners()

    def create_screens(self):
        self.main_screen = MainScreen(name = "main")
        self.password_screen = PasswordScreen(name = "password")

    def add_screens(self):
        self.add_widget(self.main_screen)
        self.add_widget(self.password_screen)

    def click_listeners(self):
        self.main_screen.btn1.on_press = self.navigate_to_password()
        self.password_screen.back_btn.on_press = self.navigate_to_main()

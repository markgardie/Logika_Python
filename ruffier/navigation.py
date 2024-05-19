from kivy.uix.screenmanager import ScreenManager


class Navigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()

    def create_screens(self):
        self.intro_screen = IntroScreen()
        

    def add_screens(self):
        pass

    def navigate_to_second(self):
        self.current = "start_pulse_screen"
        self.transition.direction = "left"
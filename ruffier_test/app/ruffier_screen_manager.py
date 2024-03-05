from kivy.uix.screenmanager import ScreenManager


class RuffierScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()

    def create_screens(self):
        self.intro_screen = IntroScreen(name = "intro_screen")
        self.rest_pulse_screen = RestPulseScreen(name = "rest_pulse_screen")
        

    def add_screens(self):
        self.add_widget(self.intro_screen)
        self.add_widget(self.rest_pulse_screen)

    def navigate_to_rest_pulse(self):
        self.current = "rest_pulse_screen"
        self.transition.direction = "left"

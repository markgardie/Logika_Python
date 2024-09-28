from kivy.uix.screenmanager import ScreenManager
from ruffier.ui.instr_screen import InstrScreen
from pulse_screen1 import PulseScreen1
from squat_screen import SquatScreen
from pulse_screen2 import PulseScreen2
from result_screen import ResultScreen

class RuffierNavigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()

    def create_screens(self):
        self.intro_screen = IntroScreen(name = "intro_screen")
        
    def add_screens(self):
        self.add_widget(self.intro_screen)

    def navigate_to_second(self):
        self.current = "start_pulse_screen"
        self.transition.direction = "left"


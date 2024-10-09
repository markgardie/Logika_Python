from kivy.uix.screenmanager import ScreenManager
from ui.instr_screen import InstrScreen
from ui.pulse_screen1 import PulseScreen1
from ui.squat_screen import SquatScreen
from ui.pulse_screen2 import PulseScreen2
from ui.result_screen import ResultScreen

class RuffierNavigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_screens()
        self.add_screens()

    def create_screens(self):
        self.instr_screen = InstrScreen(name = "instr_screen")
        self.pulse_screen1 = PulseScreen1(name = "pulse_screen1")
        
    def add_screens(self):
        self.add_widget(self.instr_screen)
        self.add_widget(self.pulse_screen1)

    def navigate_to_pulse1(self):
        self.current = "pulse_screen1"
        self.transition.direction = "left"
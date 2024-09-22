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
        self.click_listeners()

    def create_screens(self):
        self.instr_screen = InstrScreen(name = "instr_screen")

    def add_screens(self):
        self.add_widget(self.instr_screen)

    def click_listeners(self):
        self.instr_screen.btn.on_press = self.navigate_to_p1

    def navigate_to_p1(self):
        self.current = "pulse_screen1"


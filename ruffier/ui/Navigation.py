from kivy.uix.screenmanager import ScreenManager
from ui.InstructionScreen import InstructionScreen
from ui.RestPulseScreen import RestPulseScreen
from data.RuffierRepository import RuffierRepository


class Navigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.repository = RuffierRepository()

        self.create_screens()
        self.add_screens()
        self.click_listeners()

    def create_screens(self):
        self.instruction_screen = InstructionScreen(name = "instruction")
        self.rest_pulse_screen = RestPulseScreen(name = "rest_pulse")

    def add_screens(self):
        self.add_widget(self.instruction_screen)
        self.add_widget(self.rest_pulse_screen)

    def click_listeners(self):
        self.instruction_screen.start_btn.on_press = self.navigate_to_rest_pulse
    
    def navigate_to_rest_pulse(self):

        name = self.instruction_screen.name_input.text
        age = int(self.instruction_screen.age_input.text)

        self.repository.set_user(name, age)

        self.transition.direction = "left"
        self.current = "rest_pulse"
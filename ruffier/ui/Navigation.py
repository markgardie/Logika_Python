from kivy.uix.screenmanager import ScreenManager
from ui.InstructionScreen import InstructionScreen
from ui.RestPulseScreen import RestPulseScreen
from ui.SquatScreen import SquatScreen
from ui.ActivityPulseScreen import ActivityPulseScreen
from domain.User import User
from domain.Result import Result


class Navigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.result = Result()

        self.create_screens()
        self.add_screens()
        self.click_listeners()

    def create_screens(self):
        self.instruction_screen = InstructionScreen(name = "instruction")
        self.rest_pulse_screen = RestPulseScreen(name = "rest_pulse")
        self.squats_screen = SquatScreen(name = "squat")
        self.activity_pulse_screen = ActivityPulseScreen(name = "activity_pulse")

    def add_screens(self):
        self.add_widget(self.instruction_screen)
        self.add_widget(self.rest_pulse_screen)
        self.add_widget(self.squats_screen)
        self.add_widget(self.activity_pulse_screen)

    def click_listeners(self):
        self.instruction_screen.start_btn.on_press = self.navigate_to_rest_pulse
        self.rest_pulse_screen.next_btn.on_press = self.navigate_to_squat
        self.squats_screen.next_btn.on_press = self.navigate_to_activity

    
    def navigate_to_rest_pulse(self):

        name = self.instruction_screen.name_input.text
        age = int(self.instruction_screen.age_input.text)

        self.user = User(name, age)

        self.transition.direction = "left"
        self.current = "rest_pulse"

    def navigate_to_squat(self):

        self.result.rest_pulse = self.rest_pulse_screen.result_input.text

        self.transition.direction = "left"
        self.current = "squat"


    def navigate_to_activity(self):

        self.transition.direction = "left"
        self.current = "activity_pulse"
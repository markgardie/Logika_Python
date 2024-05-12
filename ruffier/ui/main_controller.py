from domain.ruffier_use_case import*
from domain.user import User


class MainController():

    def __init__(self):
        self.intro_screen = IntroScreen()


    def click_listeners(self):
        self.intro_screen.next_button.on_press = self.navigate_to_second

    
    def create_user(self):
        self.user = User(
            self.intro_screen.name_input.text,
            self.intro_screen.age_input.text
        )
    
    def save_p1(self):
        self.p1 = self.first_pulse_screen.pulse_input.text
    

    def finish(self):
        index = ruffier_index(
            self.p1,
            self.rest_pulse_screen.pulse_input2.text,
            self.rest_pulse_screen.pulse_input3.text
        )
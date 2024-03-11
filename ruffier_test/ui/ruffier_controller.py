from app.ruffier_screen_manager import RuffierScreenManager
from domain.ruffier_use_case import*
from domain.user import User

class RuffierController():

    def __init__(self):
        self.screen_manager = RuffierScreenManager()

    def click_listeners(self):
        self.screen_manager.intro_screen.next_button.on_press = self.create_user
        self.screen_manager.rest_pulse_screen.next_button.on_press = self.save_p1
        self.screen_manager.activity_pulse_screen.finish_button.on_press = self.finish

    
    def create_user(self):
        self.user = User(
            name = self.screen_manager.intro_screen.name_input.text,
            age = self.screen_manager.intro_screen.age_input.text
        )
        self.screen_manager.navigate_to_rest_pulse()
    
    def save_p1(self):
        self.p1 = self.screen_manager.rest_pulse_screen.pulse_input.text
        self.screen_manager.navigate_to_squat()
    

    def finish(self):
        index = ruffier_index(
            p1 = self.p1,
            p2 = self.screen_manager.rest_pulse_screen.activity_input.text,
            p3 = self.screen_manager.rest_pulse_screen.rest_input.text
        )

        level = get_level(index, self.user.age)

        self.screen_manager.result_screen.name_label.text = self.user.name
        self.screen_manager.result_screen.index_label.text = f"Ваш індекс: {index}"
        self.screen_manager.result_screen.level_label.text = f"Працездатність серця: {level}"

        self.screen_manager.navigate_to_result()
    

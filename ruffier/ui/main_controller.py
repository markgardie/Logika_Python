from domain.ruffier_functions import*
from domain.user import User
from app.ruffier_nav import RuffierNavigation

class MainController():

    def __init__(self):
        
        self.navigator = RuffierNavigation()


    def click_listeners(self):
        self.instr_screen.next_button.on_press = self.create_user()
        self.start_pulse_screen.next_button.on_press = self.save_p1()
        self.squat_screen.next_button.on_press = self.navigator.navigate_to_fourth()
        self.activity_pulse_screen.next_button.on_press = self.finish()
        self.result_screen.finish_button.on_press = self.navigator.navigate_to_first()


    def create_user(self):
        self.user = User(
            self.instr_screen.name_input.text,
            self.instr_screen.age_input.text
        )

        self.navigator.navigate_to_second()
    
    def save_p1(self):
        self.p1 = self.start_pulse_screen.pulse_input.text
        self.navigator.navigate_to_third()
    

    def finish(self):
        index = ruffier_index(
            self.p1,
            self.rest_pulse_screen.pulse_input2.text,
            self.rest_pulse_screen.pulse_input3.text
        )

        level = get_level(index, self.user.age)

        self.result_screen.result_label.text = f''' 
            Шановний, {self.user.name}
            Ваш індекс: {index}
            Ваш рівень: {level}
        '''

        self.navigator.navigate_to_fifth()
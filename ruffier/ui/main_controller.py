from domain.ruffier_functions import*
from domain.user import User
from app.ruffier_nav import RuffierNavigation

class MainController():

    def __init__(self):
        
        self.navigator = RuffierNavigation()


    def click_listeners(self):
        self.navigator.instr_screen.next_button.on_press = self.create_user()
        self.navigator.pulse_screen1.next_button.on_press = self.save_p1()
        self.navigator.squat_screen.next_button.on_press = self.navigator.navigate_to_pulse2()
        self.navigator.pulse_screen2.next_button.on_press = self.finish()


    def create_user(self):
        self.user = User(
            self.navigator.instr_screen.name_input.text,
            self.navigator.instr_screen.age_input.text
        )

        self.navigator.navigate_to_pulse1()
    
    def save_p1(self):
        self.p1 = self.navigator.pulse_screen1.pulse_input.text
        self.navigator.navigate_to_squat()
    

    def finish(self):
        index = ruffier_index(
            self.p1,
            self.navigator.pulse_screen2.pulse_input2.text,
            self.navigator.pulse_screen2.pulse_input3.text
        )

        level = get_level(index, self.user.age)

        self.navigator.result_screen.result_label.text = f''' 
            Шановний, {self.user.name}
            Ваш індекс: {index}
            Ваш рівень: {level}
        '''

        self.navigator.navigate_to_result()
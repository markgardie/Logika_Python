from domain.ruffier_functions import*
from domain.user import User
from app.ruffier_nav import RuffierNavigation

class MainController():

    def __init__(self):
        
        self.navigator = RuffierNavigation()


    def click_listeners(self):
        self.navigator.instr_screen.next_btn.on_press = self.create_user()
        self.navigator.pulse_screen1.next_btn.on_press = self.save_p1()
        self.navigator.squat_screen.next_btn.on_press = self.navigator.navigate_to_pulse2()
        self.navigator.pulse_screen2.next_btn.on_press = self.finish()


    def create_user(self):
        self.user = User(
            self.navigator.instr_screen.name_ti.text,
            self.navigator.instr_screen.age_ti.text,
        )

        self.navigator.navigate_to_pulse1()
    
    def save_p1(self):
        self.p1 = self.navigator.pulse_screen1.p1_ti.text
        self.navigator.navigate_to_squat()
    

    def finish(self):
        index = ruffier_index(
            int(self.p1),
            int(self.navigator.pulse_screen2.p2_ti.text),
            int(self.navigator.pulse_screen2.p3_ti.text),
        )

        level = get_level(index, self.user.age)

        self.navigator.result_screen.result_label.text = f''' 
            Шановний, {self.user.name}
            Ваш індекс: {index}
            Ваш рівень: {level}
        '''


        self.navigator.navigate_to_result()




from domain.ruffier_functions import*
from domain.user import User

class MainController():

    def __init__(self):
        pass

    def click_listeners(self):
        pass

    def create_user(self):
        self.user = User(
            self.instr_screen.ti_name.text,
            self.instr_screen.ti_age.text
        )
    
    def save_p1(self):
        self.p1 = self.pulse_screen1.ti_pulse1.text
    

    def finish(self):
        index = ruffier_index(
            self.p1,
            self.pulse_screen2.ti_pulse2.text,
            self.pulse_screen2.ti_pulse3.text
        )

        level = get_level(index, self.user.age)

        self.result_screen.lb_result.text = f'''
                Шановний, {self.user.name}
                Ваш індекс: {index}
                Працездатність серця: {level}

        '''
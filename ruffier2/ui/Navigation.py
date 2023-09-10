

class Navigation(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.result = Result()
    

        self.create_screens()
        self.add_screens()
        self.click_listeners()

    def create_screens(self):

        self.instr_screen = InstructionScreen(name = "instruction")
        self.rest_screen = RestPulseScreen(name = "rest")
        self.squat_screen = SquatScreen(name = "squat")
        self.activity_screen = ActivityPulseScreen(name = "activity")
        self.result_screen = ResultScreen(name = "result")



    def add_screens(self):
        self.add_widget(self.instr_screen)
        self.add_widget(self.rest_screen)
        self.add_widget(self.squat_screen)
        self.add_widget(self.activity_screen)
        self.add_widget(self.result_screen)


    def click_listeners(self):

        self.instr_screen.start_button.on_press = self.navigate_to_rest
        self.rest_screen.next_button.on_press = self.navigate_to_squat
        self.squat_screen.next_button.on_press = self.navigate_to_activity
        self.activity_screen.next_button.on_press = self.navigate_to_result
        

    def navigate_to_rest(self):

        self.user = User(self.instr_screen.name_input.text, int(self.instr_screen.age_input.text))
        self.current = "rest"
        self.transition.direction = "left"

    def navigate_to_squat(self):

        self.result.rest_pulse = self.rest_screen.rest_input.text

        self.current = "squat"
        self.transition.direction = "left"

    def navigate_to_activity(self):

        self.current = "activity"
        self.transition.direction = "left"

    def navigate_to_result(self):

        self.result.activity_pulse = self.activity_screen.activity_input.text
        self.result.end_pulse = self.activity_screen.end_input.text

        self.result.calculate_ruffier()
        self.result.bad_level()
        self.result.calculate_result()
        self.show_result()

        self.current = "result"
        self.transition.direction = "left"

    def show_result(self):

        self.result_screen.name_label.text = self.user.name
        self.result_screen.ruffier_label.text = f"Ваш індекс Руф'є: {self.result.ruffier_index}"
        
        if self.result.final_result == 0:
            level = "Погана"


    

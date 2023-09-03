

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


    def add_screens(self):
        self.add_widget(self.instr_screen)
        self.add_widget(self.rest_screen)
        self.add_widget(self.squat_screen)

    def click_listeners(self):

        self.instr_screen.start_button.on_press = self.navigate_to_rest
        self.rest_screen.next_button.on_press = self.navigate_to_squat
from app.ruffier_screen_manager import RuffierScreenManager

class RuffierController():

    def __init__(self):
        self.screen_manager = RuffierScreenManager()

    def click_listeners(self):
        self.screen_manager.intro_screen.next_button.on_press = self.screen_manager.navigate_to_rest_pulse
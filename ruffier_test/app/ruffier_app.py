from kivy.app import App
from app.ruffier_screen_manager import RuffierScreenManager

class RuffierApp(App):

    def build(self):

        return RuffierScreenManager()
    

RuffierApp().run()
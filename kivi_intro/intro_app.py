from kivy.app import App
from intro_screen_manager import IntroScreenManager

class IntroApp(App):

    def build(self):

        return IntroScreenManager()
    

IntroApp().run()

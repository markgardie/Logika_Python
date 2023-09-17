from kivy.app import App
from ui.Navigation import Navigation


class RuffierApp(App):

    def build(self):
        return Navigation()
    

RuffierApp().run()
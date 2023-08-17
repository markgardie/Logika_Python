from kivy.app import App
from ui.Navigation import Navigation

class FirstApp(App):

    def build(self):
        return Navigation()
    

FirstApp().run()

from kivy.app import App
from ruffier_nav import RuffierNavigation

class RuffierApp(App):
    def build(self):
        return RuffierNavigation()
    
RuffierApp().run()
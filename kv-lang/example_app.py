from kivy.app import App
from kivy.lang import Builder
from example_sm import ExampleScreenManager

Builder.load_file('kv-lang\example.kv')

class ExampleApp(App):

    def build(self):
        return ExampleScreenManager()
    
ExampleApp.run()
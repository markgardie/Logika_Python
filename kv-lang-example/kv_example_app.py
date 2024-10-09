import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

Builder.load_file('kv-lang\kv_example.kv')

class MyScreenManager(ScreenManager):
    def navigate_to_second(self):
        self.current = "second_screen"
        self.transition.direction = "left"

    def navigate_to_first(self):
        self.current = "first_screen"
        self.transition.direction = "left"


class MyApp(App): # <- Main Class
    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    MyApp().run()
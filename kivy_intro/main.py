from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

class MenuScreen(Screen):

    def go_game(self):
        self.manager.current = "game"

    def go_settings(self):
        self.manager.current = "settings"

    def exit_game(self):
        App.get_running_app().stop()

class SettingsScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class ClickerApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(Menu(name = "menu"))
        sm.add_widget(Settings(name = "settings"))
        sm.add_widget(Game(name = "game"))

        return sm


app = ClickerApp()
app.run()
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

INFO_TEXT = "Натисніть на кнопку нижче, аби переключитись на наступний екран"
NEXT_BTN_TEXT = "Далі"

class Screen1(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_widgets()
        self.create_layouts()
        self.setup_layout()

    def create_widgets(self):
        self.password_label = Label()
        self.password_input = TextInput()
        self.ok_button = Button()
        self.back_button = Button()

    def create_layouts(self):
        self.row = BoxLayout()

    def setup_layout(self):
        self.row.add_widget(self.password_label)
        self.row.add_widget(self.password_input)
        self.row.add_widget(self.ok_button)
        self.row.add_widget(self.back_button)

        self.add_widget(self.row)
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from utils.Constants import*

class RestPulseScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_widgets()
        self.create_layouts()
        self.setup_layout()

    def create_widgets(self):
        self.instr_label = Label(text = TEST1)

        self.result_hint = Label(text = "Введіть результат", halign='right') 
        self.result_input = TextInput(multiline=False)    

        self.next_btn = Button(text = "Продовжити", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

    def create_layouts(self):
        self.main_column = BoxLayout(orientation = "vertical", padding=8, spacing=8)

        self.result_row = BoxLayout(size_hint=(0.8, None), height='30sp')

    def setup_layout(self):
        self.result_row.add_widget(self.result_hint)
        self.result_row.add_widget(self.result_input)

        self.main_column.add_widget(self.instr_label)
        self.main_column.add_widget(self.result_row)
        self.main_column.add_widget(self.next_btn)

        self.add_widget(self.main_column)
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from utils.Constants import*

class ActivityPulseScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_widgets()
        self.create_layouts()
        self.setup_layout()

    def create_widgets(self):
        self.activity_pulse_label = Label(text = TEST3)

        self.activity_hint = Label(text = "Результат")
        self.rest_hint = Label(text = "Результат після відпочинку")

        self.activity_input = TextInput(multiline = False)
        self.rest_input = TextInput(multiline = False)

        self.finish_btn = Button(text = "Завершити", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})

       
    def create_layouts(self):
        self.activity_row = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.rest_row = BoxLayout(size_hint=(0.8, None), height='30sp')

        self.main_column = BoxLayout(orientation='vertical', padding=8, spacing=8)

    def setup_layout(self):
        self.activity_row.add_widget(self.activity_hint)
        self.activity_row.add_widget(self.activity_input)

        self.rest_row.add_widget(self.rest_hint)
        self.rest_row.add_widget(self.rest_input)

        self.main_column.add_widget(self.activity_pulse_label)
        self.main_column.add_widget(self.activity_row)
        self.main_column.add_widget(self.rest_row)
        self.main_column.add_widget(self.finish_btn)

        self.add_widget(self.main_column)

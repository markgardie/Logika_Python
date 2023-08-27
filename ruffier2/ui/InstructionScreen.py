from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from Constants import*

class InstructionScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_widgets()
        self.create_layouts()
        self.setup_layout()

    def create_widgets(self):
        self.instruction_label = Label(text = INSTRUCTION)

        self.name_hint = Label(text = "Введіть ім'я")
        self.age_hint = Label(text = "Введіть вік")

        self.name_input = TextInput(multiline = False)
        self.age_input = TextInput(multiline = False)

        self.start_button = Button(text = "Почати")


    def create_layouts(self):
        self.name_row = BoxLayout()
        self.age_row = BoxLayout()

        self.main_column = BoxLayout(orientation = "vertical")
       

    def setup_layout(self):
        self.name_row.add_widget(self.name_hint)
        self.name_row.add_widget(self.name_input)

        self.age_row.add_widget(self.age_hint)
        self.age_row.add_widget(self.age_input)

        self.main_column.add_widget(self.instruction_label)
        self.main_column.add_widget(self.name_row)
        self.main_column.add_widget(self.age_row)
        self.main_column.add_widget(self.start_button)

        self.add_widget(self.main_column)
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
        self.instr_label = Label(text = TEST3)
        self.activity_label = Label(text = "Результат:")
        self.end_label = Label(text = "Результат після відпочинку")

        self.activity_input = TextInput(multiline = False)
        self.end_input = TextInput(multiline = False)
        
        self.next_button = Button(text = "Завершити")

    def create_layouts(self):
        self.main_column = BoxLayout(orientation = "vertical")
        self.activity_row = BoxLayout()
        self.end_row = BoxLayout()

    def setup_layout(self):
        self.activity_row.add_widget(self.activity_label)
        self.activity_row.add_widget(self.activity_input)

        self.end_row.add_widget(self.end_label)
        self.end_row.add_widget(self.end_input)

        self.main_column.add_widget(self.instr_label)
        self.main_column.add_widget(self.activity_row)
        self.main_column.add_widget(self.end_row)
        self.main_column.add_widget(self.next_button)

        self.add_widget(self.main_column)

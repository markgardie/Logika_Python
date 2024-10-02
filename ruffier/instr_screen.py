from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

class InstrScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets()
        self.create_layouts()
        self.setup_layout()
        
    def create_widgets(self):
        self.instr_lb = Label(text = "")
        self.name_lb = Label(text = "")
        self.age_lb = Label(text = "")

        self.name_ti = TextInput(multiline = False)
        self.age_ti = TextInput(text = "7", multiline = False)

        self.next_btn = Button(text = "Почати", 
                               size_hint = (0.3, 0.2), 
                               pos_hint = {"center_x": 0.5})    


    def create_layouts(self):
        self.name_row = BoxLayout(size_hint = (0.8, None), height = "30sp") 
        self.age_row = BoxLayout(size_hint = (0.8, None), height = "30sp")
        self.main_column = BoxLayout(orientation = "vertical")  

    def setup_layout(self):
        self.name_row.add_widget(self.name_lb)
        self.name_row.add_widget(self.name_ti)

        self.age_row.add_widget(self.age_lb)
        self.age_row.add_widget(self.age_ti)

        self.main_column.add_widget(self.instr_lb)
        self.main_column.add_widget(self.name_row)
        self.main_column.add_widget(self.age_row)
        self.main_column.add_widget(self.next_btn)

        self.add_widget(self.main_column)
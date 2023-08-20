from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen


class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets()
        self.create_layouts()
        self.set_layout()

    def create_widgets(self):
        self.hint_label = Label(text = "Обери вікно")
        self.btn1 = Button(text = "1")
        self.btn2 = Button(text = "2")
        self.btn3 = Button(text = "3")
        self.btn4 = Button(text = "4")  

    def create_layouts(self):
        self.hint_column = BoxLayout(orientation = "vertical")
        self.button_column = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)

        self.main_row = BoxLayout()

    def set_layout(self):
        self.hint_column.add_widget(self.hint_label)

        self.button_column.add_widget(self.btn1)
        self.button_column.add_widget(self.btn2)
        self.button_column.add_widget(self.btn2)
        self.button_column.add_widget(self.btn4)

        self.main_row.add_widget(self.hint_column)
        self.main_row.add_widget(self.button_column)

        self.add_widget(self.main_row)


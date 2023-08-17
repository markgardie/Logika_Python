from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

class TextInputScreen(Screen):

    def __init__(self, **kwwargs):
        super().__init__(**kwwargs)

        self.create_widgets()
        self.create_layouts()
        self.setup_layout()
        self.click_listeners()

    def create_widgets(self):
        self.screen_header = Label(text = "Екран 2")
        self.password_label = Label(text = "Введіть пароль")
        self.password_text_input = TextInput(multiline = False)
        self.back_button = Button(text = "Назад")
        self.ok_button = Button(text = "ОК")

    def create_layouts(self):
        self.main_column = BoxLayout(orientation = "vertical")
        self.password_row = BoxLayout(size_hint = (0.8, None), padding = "16sp")
        self.buttons_row = BoxLayout(size_hint = (0.5, None), pos_hint = {'center_x': 0.5})

    def setup_layout(self):
        self.password_row.add_widget(self.password_label)
        self.password_row.add_widget(self.password_text_input)

        self.buttons_row.add_widget(self.back_button)
        self.buttons_row.add_widget(self.ok_button)

        self.main_column.add_widget(self.screen_header)
        self.main_column.add_widget(self.password_row)
        self.main_column.add_widget(self.buttons_row)

        self.add_widget(self.main_column)

    def click_listeners(self):
        self.ok_button.on_press = self.change_header

    def change_header(self):
        self.screen_header.text = self.password_text_input.text + " ? Не спрацювало"
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

INFO_TEXT = "Натисніть на кнопку нижче, аби переключитись на наступний екран"
NEXT_BTN_TEXT = "Далі"

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_widgets()
        self.create_layouts()
        self.setup_layout()

    def create_widgets(self):
        self.info_label = Label(text = INFO_TEXT)
        self.next_button = Button(text = NEXT_BTN_TEXT)

    def create_layouts(self):
        self.column = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)

    def setup_layout(self):
        self.column.add_widget(self.info_label)
        self.column.add_widget(self.next_button)

        self.add_widget(self.column)

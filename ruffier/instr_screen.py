from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

class InstrScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
        
    def create_widgets(self):
        self.lb_instruction = Label(text='Інструкція')
        self.lb_name = Label(text="Введіть ім'я:")
        self.lb_age = Label(text='Введіть вік:')
        self.ti_name = TextInput(multiline = False)
        self.ti_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Почати', size_hint=(0.3,0.2), pos_hint={'center_x':0.5})

    def create_layouts(self):
        self.bl_line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        self.bl_line2 = BoxLayout(size_hint=(0.8, None), height='30sp')

        self.main_line = BoxLayout(orientation='vertical')

    def setup_layout(self):
        self.bl_line1.add_widget(self.lb_name)
        self.bl_line1.add_widget(self.ti_name)
        self.bl_line2.add_widget(self.lb_age)
        self.bl_line2.add_widget(self.ti_age)

        self.main_line.add_widget(self.lb_instruction)
        self.main_line.add_widget(self.bl_line1)
        self.main_line.add_widget(self.bl_line2)
        self.main_line.add_widget(self.btn)

        self.add_widget(self.main_line)
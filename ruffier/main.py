#pip install kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lb_instruction = Label(text='Інструкція')
        lb_name = Label(text="Введіть ім'я:")
        lb_age = Label(text='Введіть вік:')
        ti_name = TextInput(multiline = False)
        ti_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Почати', size_hint=(0.3,0.2), pos_hint={'center_x':0.5})
        bl_line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        bl_line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        bl_line1.add_widget(lb_name)
        bl_line1.add_widget(ti_name)
        bl_line2.add_widget(lb_age)
        bl_line2.add_widget(ti_age)

        main_line = BoxLayout(orientation='vertical')
        main_line.add_widget(lb_instruction)
        main_line.add_widget(bl_line1)
        main_line.add_widget(bl_line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

        self.btn.on_press = self.next

    def next(self):
        self.manager.current = 'pulse1'

class PulseScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw) 
    #label для інструкція
    #label для "Введіть результат"
    #TextInput для введення результату
    #Button       

class HeartChecker(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        return sm

app = HeartChecker()
app.run()







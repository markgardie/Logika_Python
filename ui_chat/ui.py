from customtkinter import *

class MainWindow(CTk):

    def __init__(self):
        super().__init__()

        self.geometry('400x300')
        self.title('LogiTalk')

        self.username = "Mark"

        # Меню
        self.label = None
        self.menu_frame = CTkFrame(self, width=30, height=300)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)
        self.is_show_menu = False
        self.menu_animation_speed = -20
        self.menu_btn = CTkButton(self, text="▶️", command=self.toggle_menu, width=30)
        self.menu_btn.place(x=0, y=0)

        # Поле чату
        self.chat_frame = CTkScrollableFrame(self)
        self.chat_frame.place(x=0, y=0)
        
        # Поле ведення та кнопки
        self.message_entry = CTkEntry(self, 
                                      placeholder_text="Введіть повідомлення", 
                                      height=40)
        self.message_entry.place(x=0, y=0)

        self.send_btn = CTkButton(self, text = "->", width=50, )



    def toggle_menu():
        pass

    def show_menu():
        pass

    def adaptive_ui():
        pass

    def add_message():
        pass


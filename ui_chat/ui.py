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



    def toggle_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.menu_animation_speed *= -1
            self.menu_btn.configure(text = '▶️')
            self.show_menu()
        else:
            self.is_show_menu = True
            self.menu_animation_speed *= -1
            self.menu_btn.configure(text = '◀️')
            self.show_menu()

            self.label = CTkLabel(self.menu_frame, text = "Ім'я")
            self.label.pack(pady = 30)
            self.name_entry = CTkEntry(self.menu_frame)
            self.message_entry.pack()


    def show_menu(self):
        self.menu_frame.configure(width = self.menu_frame.winfo_width() + self.menu_animation_speed)
        if not self.menu_frame.winfo_width() >= 200 and self.is_show_menu:
            self.after(10, self.show_menu)
        elif self.menu_frame.winfo_width() >= 40 and not self.is_show_menu:
            self.after(10, self.show_menu)
            if self.label and self.name_entry:
                self.label.destroy()
                self.name_entry.destroy()

    def adaptive_ui(self):
        self.menu_frame.configure(height = self.winfo_height)
        self.chat_field.place(x = self.menu_frame.winfo_width())
        self.chat_field.configure(width = self.winfo_width() - self.menu_frame.winfo_width())

    def add_message(self, text):
        self.chat_field.configure(state="normal")
        self.chat_field.insert(END, "Я:" + text + "\n")
        self.chat_field.configure(state="disable")


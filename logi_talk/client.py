from customtkinter import *
import socket
import threading

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')
        self.label = None
        # menu frame
        self.menu_frame= CTkFrame(self, width=30, height=300)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)
        self.is_show_menu = False
        self.speed_animate_menu = -5
        self.btn = CTkButton(self, text='▶️', command=self.toggle_show_menu, width=30)
        self.btn.place(x=0, y=0)
        #main
        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.place(x=0, y=0)
        self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення:', height=40)
        self.message_entry.place(x=0, y=0)
        self.send_button = CTkButton(self, text='>', width=50, height=40)
        self.send_button.place(x=0, y=0)

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except Exception as e:
            self.add_message(f"Помилка: {e}")

        self.adaptive_ui()


    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu *= -1
            self.btn.configure(text = '▶️')
            self.show_menu()
        else:
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configure(text = '◀️')
            self.show_menu()

            self.label = CTkLabel(self.menu_frame, text='Імʼя')
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.menu_frame)
            self.entry.pack()
   


    def show_menu(self):
        self.menu_frame.configure(
            width = self.menu_frame.winfo_width + self.speed_animate_menu
             )
        if not self.menu_frame.winfo_width >= 200 and self.is_show_menu:
            self.after(10, self.show_menu)
        elif self.menu_frame.winfo_width >= 40 and not self.is_show_menu:
            self.after(10, self.show_menu)
            if self.label and self.entry:
                self.label.destroy()
                self.entry.destroy()


    def adaptive_ui(self):
        self.menu_frame.configure(height = self.winfo_height())
        self.chat_field.place(x = self.winfo_width())
        self.chat_field.configure(
            width = self.winfo_width() - self.menu_frame.winfo_width() - 20,
            height = self.winfo_height() - 40
        )


    def recv_message(self):
        buffer = ""
        while True:
            try:
                chunk = self.socket.recv(4096)
                if not chunk:
                    break
                buffer += chunk.decode()

                while "\n" in buffer:
                    line, buffer = buffer.split("\n")
                    self.handle_line(line)
            except:
                break
        self.socket.close()


    def handle_line(self, line):
        if not line:
            return

        parts = line.split("@", 3)
        msg_type = parts[0]

        if msg_type == "TEXT":
            if len(parts) >= 3:
                author = parts[1]
                message = parts[2]
                self.add_message(f"{author}: {message}")

        elif msg_type == "IMAGE":
            if len(parts) >= 4:
                author = parts[1]
                filename = parts[2]
                self.add_message(f"{author}: {filename}")

        else:
            self.add_message(line)



    win = MainWindow()
    win.mainloop()


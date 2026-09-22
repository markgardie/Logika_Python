# ui.py
from customtkinter import CTk, CTkFrame, CTkButton, CTkTextbox, CTkEntry, CTkLabel, END
import tkinter as tk

class MainWindow(CTk):
    def __init__(self, client, default_username="User"):
        super().__init__()
        self.title("Chat (текст)")
        self.geometry("600x400")
        self.minsize(400, 300)

        self.client = client  # екземпляр ChatClient
        self.username = tk.StringVar(value=default_username)

        # --- layout ---
        # menu frame (ліва панель)
        self.menu_frame = CTkFrame(self, width=200)
        self.menu_frame.pack(side="left", fill="y")

        CTkLabel(self.menu_frame, text="Ім'я:").pack(pady=(20, 4))
        self.name_entry = CTkEntry(self.menu_frame, textvariable=self.username)
        self.name_entry.pack(fill="x", padx=10)

        CTkLabel(self.menu_frame, text="").pack(pady=(10, 0))  # spacer

        # праворуч — чат
        right_frame = CTkFrame(self)
        right_frame.pack(side="left", fill="both", expand=True)

        self.chat_field = CTkTextbox(right_frame, wrap="word", state="disabled")
        self.chat_field.pack(fill="both", expand=True, padx=8, pady=(8, 4))

        bottom_frame = CTkFrame(right_frame, height=40)
        bottom_frame.pack(fill="x", padx=8, pady=(0, 8))

        self.message_entry = CTkEntry(bottom_frame, placeholder_text="Введіть повідомлення...")
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

        self.send_button = CTkButton(bottom_frame, text="Відправити", width=120, command=self.on_send)
        self.send_button.pack(side="right")

        # bind Enter
        self.message_entry.bind("<Return>", self._enter_pressed)

        # при закритті вікна треба закрити клієнт
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # невеликий внутрішній буфер для автоскролу
        self._at_bottom = True
        self.chat_field.bind("<MouseWheel>", self._on_scroll_mousewheel)

    # UI-інтерфейс, який викликає потік recv через ui.after
    def add_message(self, author: str, text: str):
        """Додає повідомлення у текстове поле. Викликається з головного потоку через after."""
        self.chat_field.configure(state="normal")
        # просте форматування: якщо автор — наше ім'я, покажемо "Я"
        display_author = "Я" if author == self.username.get() else author
        self.chat_field.insert(END, f"{display_author}: {text}\n")
        # автоскрол
        self.chat_field.see("end")
        self.chat_field.configure(state="disabled")

    # callback потоку (вище в client.start_receiving викликає цей колбек)
    def on_incoming_message(self, author, message):
        # Безпечне оновлення UI: schedule on main thread
        self.after(0, self.add_message, author, message)

    # відправка повідомлення
    def on_send(self):
        text = self.message_entry.get().strip()
        if not text:
            return
        username = self.username.get().strip() or "User"
        try:
            self.client.send_text(username, text)
            # локально додамо повідомлення (щоб не чекати ретрансляції серверу)
            self.add_message(username, text)
        except Exception as e:
            # показуємо помилку у чаті
            self.add_message("SYSTEM", f"Не вдалось надіслати повідомлення: {e}")
        finally:
            # очистити поле та фокус
            self.message_entry.delete(0, END)
            self.message_entry.focus_set()

    def _enter_pressed(self, event):
        self.on_send()
        return "break"

    def on_close(self):
        # закриваємо клієнт та вікно
        try:
            self.client.close()
        except Exception:
            pass
        self.destroy()

    def _on_scroll_mousewheel(self, event):
        # простий індикатор прокрутки
        self._at_bottom = False

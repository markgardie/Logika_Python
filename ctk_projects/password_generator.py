from customtkinter import *
from random import *


def show_diff_pass(value):
   global diff_password
   diff_password = int(value)
   count_password_chars_label.configure(text=f'{int(value)}')
   generate_password()


def generate_password():
    global diff_password
    chars = [char for char in 'qwertyuiopasdfghjklzxcvbnm']
    spec_chars = [char for char in '!@#$%^&*()_+']
    available_value = []
    result = ''

    if l_chars_btn.get():
        available_value += chars
    if up_chars_btn.get():
        available_value += chars.upper()
    if spec_chars_btn.get():
        available_value += spec_chars
    if number_char_btn.get():
        available_value += [str(i) for i in range(0, 10)]

    for i in range(diff_password):
        result += choice(available_value)

    password_entry.delete(0, "end")
    password_entry.insert(0, result)


diff_password = 4
window = CTk()
window.geometry("400x300")
window.maxsize(400, 300)
window.title('GP')


set_appearance_mode('dark')
set_default_color_theme('green')

settings_frame_left = CTkFrame(window, width=200)
settings_frame_left.grid(row = 1, column = 0)

settings_frame_right = CTkFrame(window)
settings_frame_right.grid(row = 1, column = 1)

l_chars_btn = CTkCheckBox(settings_frame_left, text = "Маленькі літери", width = 220)
up_chars_btn = CTkCheckBox(settings_frame_left, text = "Великі літери", width = 220)
numbers_chars_btn = CTkCheckBox(settings_frame_left, text = "Цифри", width = 220)
spec_chars_btn = CTkCheckBox(settings_frame_left, text = "Спеціальні символи", width = 220)

l_chars_btn.pack(pady = 5)
up_chars_btn.pack(pady = 5)
numbers_chars_btn.pack(pady = 5)
spec_chars_btn.pack(pady = 5)

window.mainloop()

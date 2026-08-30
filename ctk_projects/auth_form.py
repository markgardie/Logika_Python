from customtkinter import *
from PIL import Image


class AuthWindow(CTk):
   def __init__(self):
        super().__init__()
        self.geometry('700x400')
        self.title('Вхід')
        self.resizable(True, False)

        # --- ліва частина --
        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side = "left", fill = "both")

        image = Image.open("ctk_projects\images\bg.png")
        self.ctk_image = CTkImage(image = image, size = (450, 400))

        self.image_label = CTkLabel(
            self.left_frame,
            text = "Welcome", 
            image = self.ctk_image,
            font = ('Helvetica', 60, 'bold')
            )

        self.image_label.pack()

        # -- ПРАВА ЧАСТИНА----
        main_font = ('Helvetica', 20, 'bold')
        self.right_frame = CTkFrame(self)
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side = "right", fill = "both", expand = True)

        self.title_label = CTkLabel(
            self.right_frame, 
            text = "LogiTalk", 
            font = main_font,
            text_color = '#6753cc'
            )
        self.title_label.pack(pady = 60)

        self.name_entry = CTkEntry(
            self.right_frame,
            placeholder_text= '☻ ім`я',
            height= 40,
            font = main_font,
            corner_radius= 25,
            fg_color= '#eae6ff',
            border_color= '#eae6ff',
            text_color= '#6753cc',
            placeholder_text_color= '#6753cc',
        )
        self.name_entry.pack(fill = "x", padx = 10)


window = AuthWindow()
window.mainloop()

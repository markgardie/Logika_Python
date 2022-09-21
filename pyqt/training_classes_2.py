class Title():
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True
    def hide(self):
        self.appearance = False
        print(self.title, '- приховано')
    def show(self):
        self.appearance = True
        print(self.title, '- відображається')
    def print_info(self):
        print('Кнопка:', self.title)
        print('Розташування:', '(' + str(self.x) + ',' + str(self.y) + ')')
        print('Видимість:', self.appearance)
 
main_title = Title('Дізнатися переможця прямо зараз!', 150, 50)
rules_title = Title('Переможець може бути тільки один', 150, -100)
main_title.print_info()
rules_title.print_info()
rules_title.hide()

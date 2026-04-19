from turtle import *


speed(0)
screen = getscreen()
screen.bgcolor("black")

# базові графічні примітиви
# Функція для швидкого переміщення черепашки
def go_xy(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_line(t, x1, y1, x2, y2, cl="green"):
    t.color(cl)
    go_xy(t, x1, y1)
    t.goto(x2, y2)


def draw_rect(t, x, y, w, h, fill=None):
    go_xy(t, x, y)
    if fill:
        t.color(fill)
        begin_fill()
    t.setheading(0)
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    if fill:
        end_fill()


# Функції для створення потрібних об'єктів редактора
# створення пера
def create_pen():
    pen = Turtle()
    pen.color("blue")
    pen.speed(0)
    pen.shape("circle")


    # функції пера
    def on_key_left():
        pen.setheading(180)
        pen.forward(10)


    def on_key_right():
        pen.setheading(0)
        pen.forward(10)


    def on_key_up():
        pen.setheading(90)
        pen.forward(10)


    def on_key_down():
        pen.setheading(-90)
        pen.forward(10)
       
    def set_red():
        pen.color("red")


    def set_green():
        pen.color("green")


    def set_blue():
        pen.color("blue")


    pen.set_red = set_red
    pen.set_green = set_green
    pen.set_blue = set_blue


    pen.on_key_left = on_key_left
    pen.on_key_right = on_key_right
    pen.on_key_up = on_key_up
    pen.on_key_down = on_key_down


    return pen

# позначка, показує результат (скільки кліків і скільки черепашок втекли)
def create_label(x,y, cl, text):
    t = Turtle()
    go_xy(t, x, y)
    t.color(cl)
    t.write(text, font=("Arial", 16, "normal"))
    t.hideturtle()
    return t


# кнопка керування
def create_button(x,y, cl, shape = "square"):
    t = Turtle()
    t.shape(shape)
    go_xy(t, x, y)
    t.color(cl)
    return t


# індікатор стану
def create_indicator(x,y, active):
    t = Turtle()
    t.speed(0)
    t.shape("circle")
    go_xy(t, x, y)


    def set_active(active):
        if active:
            t.color("red")
        else:
            t.color("gray")


    t.active = set_active
    t.active(active)


    return t
   

# поле для рисування
def create_field():
    draw_rect(getpen(), -200, 120, 400, 320, "white")

# об'єкти редактора та їх налаштування
create_field()
draw_rect(getpen(),-200, 200, 400, 70, "green")
pen = create_pen()

def on_screen_click(x, y):
    if y > 120:
        return
    go_xy(pen, x, y)

def on_drag(x, y):
    if y > 120:
        return
    pen.goto(x, y)

# панель керування і об'єкти
btn_width_up = create_button(100, 180, "red")
btn_width_down = create_button(100, 150, "blue")
btn_clear = create_button(-80, 165, "orange")
width_label = create_label(130, 150, "black", f"W: {pen.width()}")


def on_width_up(x, y):
    w = pen.width()
    if w < 10:
        pen.width(w + 1)
        width_label.clear()
        width_label.write(f"W: {w + 1}", False, font=("Arial", 16, "normal"))

def on_width_down(x, y):
    w = pen.width()
    if w > 1:
        pen.width(w - 1)
        width_label.clear()
        width_label.write(f"W: {w - 1}", False, font=("Arial", 16, "normal"))

def on_clear(x, y):
    pen.clear()


btn_clear.onclick(on_clear)
btn_width_up.onclick(on_width_up)
btn_width_down.onclick(on_width_down)


fill_label = create_label(-50, 150, "white", f"Заливка:")
clear_label = create_label(-190, 150, "white", f"Очистити:")
fill_indicator = create_indicator(50, 165, False)


def on_begin_fill():
    pen.begin_fill()
    fill_indicator.active(True)


def on_end_fill():
    pen.end_fill()
    fill_indicator.active(False)


# Підписуємось на натиск клавіш та події кліку/ перетягування
screen.onkey(pen.on_key_left, "Left")
screen.onkey(pen.on_key_right, "Right")
screen.onkey(pen.on_key_up, "Up")
screen.onkey(pen.on_key_down, "Down")


screen.onkey(pen.set_red, "r")
screen.onkey(pen.set_green, "g")
screen.onkey(pen.set_blue, "b")
screen.onkey(pen.clear, "space")
screen.onkey(on_begin_fill, "o")
screen.onkey(on_end_fill, "p")


pen.ondrag(on_drag)
screen.onclick(on_screen_click)
screen.listen()

done()

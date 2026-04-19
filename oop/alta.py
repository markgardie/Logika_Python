from turtle import *

speed(0)
screen = getscreen()
screen.bgcolor("black")

colors = ["red", "Crimson", "Firebrick", "DarkRed", "RoyalBlue", "Blue",
            "Navy", "MidnightBlue", "LawnGreen", "Lime", "YellowGreen",
            "OliveDrab", "SpringGreen", "Green", "DarkGreen", "Cyan",
            "DarkTurquoise", "LightSeaGreen", "CadetBlue", "White", 
            "Gainsboro", "Silver", "DarkGray", "Gray", "DimGray", 
            "Black", "LemonChiffon", "Yellow", "Gold", "Goldenrod", 
            "DarkGoldenrod", "Burlywood", "Peru", "Sienna", "SaddleBrown", 
            "LightPink", "HotPink", "DeepPink", "PaleVioletRed", 
            "MediumVioletRed", "Purple", "DarkMagenta", "Magenta", 
            "DarkOrchid", "BlueViolet", "MediumPurple", "RebeccaPurple", 
            "Indigo", "Bisque", "PeachPuff", "NavajoWhite", "Wheat", "Tan", 
            "AntiqueWhite", "FloralWhite", "Moccasin", ]

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

def create_pen():
    pen = Turtle()
    pen.color("black")
    pen.shape("circle")
    pen.speed(0)
    def on_key_left():
        new_x = pen.xcor() - 10
        if new_x < -200:
            return
        pen.goto(new_x, pen.ycor())
    def on_key_right():
        new_x = pen.xcor() + 10
        if new_x > 200:
            return
        pen.goto(new_x, pen.ycor())
    def on_key_up():
        new_y = pen.ycor() + 10
        if new_y > 120:
            return
        pen.goto(pen.xcor(), new_y)
    def on_key_down():
        new_y = pen.ycor() - 10
        if new_y < -200:
            return
        pen.goto(pen.xcor(), new_y)
    pen.on_key_left = on_key_left
    pen.on_key_right = on_key_right
    pen.on_key_up = on_key_up
    pen.on_key_down = on_key_down
    return pen
    
def create_label(x,y, cl, text):
    t = Turtle()
    t.speed(0)
    go_xy(t, x, y)
    t.color(cl)
    t.write(text, font=("Arial", 16, "normal"))
    t.hideturtle()
    return t

def create_button(x,y, cl, shape = "square"):
    t = Turtle()
    t.speed(0)
    t.shape(shape)
    go_xy(t, x, y)
    t.color(cl)
    return t
    
def create_indicator(x, y, active):
    t = Turtle()
    t.speed(0)
    go_xy(t, x, y)
    t.shape("circle")
    def set_active(active):
        if active:
            t.color("red")
        else:
            t.color("grey")
    t.active = set_active
    t.active(active)
    return t

def create_field():
    draw_rect(getpen(), -200, 120, 400, 320, "white")

create_field()
draw_rect(getpen(),-200, 200, 400, 70, "green")
pen = create_pen()

def on_screen_click(x, y):
    if y > 120 or x > 200 or y < -200 or x < -200:
        return
    go_xy(pen, x, y)
    
def on_drag(x, y):
    if y > 120 or x > 200 or y < -200 or x < -200:
        return
    pen.goto(x, y)
    
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
#fill = False

#def on_fill():
#    global fill

def on_begin_fill():
    pen.begin_fill()
    fill_indicator.active(True)
    
def on_end_fill():
    pen.end_fill()
    fill_indicator.active(False)
    
screen.onkey(pen.on_key_left, "a")
screen.onkey(pen.on_key_up, "w")
screen.onkey(pen.on_key_down, "s")
screen.onkey(pen.on_key_right, "d")

def click(x, y, col):
    tt = Turtle()
    tt.speed(0)
    tt.penup()
    tt.color(col)
    tt.shape("square")
    tt.goto(x, y)
    def set_color(x, y):
        pen.color(col)
    tt.onclick(set_color)
    
x = 230
y = 110

for color in colors:
    click(x, y, color)
    y -= 20
    if y <= -160:
        y = 110
        x += 20
        
def write(x, y):
    ttt = Turtle()
    ttt.speed(0)
    ttt.penup()
    ttt.goto(x, y)
    ttt.pendown()
    ttt.width(6)
    ttt.color("green")
    ttt.left(90)
    ttt.bk(15)
    ttt.fd(15)
    ttt.rt(90)
    ttt.fd(10)
    ttt.bk(20)
    ttt.fd(10)
    ttt.left(90)
    ttt.bk(10)
    ttt.hideturtle()
    ttt.shape("square")
   
    def write_1(x, y):
        a = input("Введіть текст: ")
        pen.write(a, font=("Arial", 20))
    ttt.onclick(write_1)

#screen.onkey(lambda : pen.color("red"), "r")
#screen.onkey(lambda : pen.color("green"), "g")
#screen.onkey(lambda : pen.color("blue"), "b")
#screen.onkey(lambda : pen.color("orange"), "o")
#screen.onkey(lambda : pen.color("purple"), "p")
#screen.onkey(lambda : pen.color("yellow"), "y")
#screen.onkey(lambda : pen.color("black"), "1")
#screen.onkey(lambda : pen.color("grey"), "2")
#screen.onkey(lambda : pen.color(""), "2")

write(-230, 110)
screen.onkey(on_begin_fill, "3")
screen.onkey(on_end_fill, "4")
pen.ondrag(on_drag)
screen.onclick(on_screen_click)

screen.listen()
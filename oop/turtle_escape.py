from turtle import *
from random import randint
screen = getscreen()
speed(0)
hideturtle()


# функції для роботи програми
def go_xy(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# створення черепашки, яка буде тікати
def create_turtle(x, y, cl):
    t = Turtle()
    t.color(cl)
    t.shape("turtle")
    t.setheading(randint(0,360))
    t.penup()
    t.goto(x, y)
    t.pendown()
    go_xy(t, x, y)
    return t


# позначка, показує результат (скільки кліків і скільки черепашок втекли)
def create_label(x,y, cl, text):
    t = Turtle()
    go_xy(t, x, y)
    t.color(cl)
    t.write(text, font=("Arial", 16, "normal"))
    t.hideturtle()
    return t


def create_field():
    color("#FFFF00")
    go_xy(getpen(), -200, -200)
    begin_fill()
    for i in range(4):
        forward(400)
        left(90)
    end_fill()
       
def is_turtle_inside(t):
    if -200 < t.xcor() < 200:
        if -200 < t.ycor() < 200:
            return True


    return False

####################################################
# сама гра
clicks = 0
turtles_outside = 0


clickLabel = create_label(-180, 220, "blue", f"Кліки: {clicks}")
turtlesLabel = create_label(100, 220, "red", f"Втечі: {turtles_outside}")


create_field()
t1 = create_turtle(50,50,"red")
t2 = create_turtle(50,-50,"green")
t3 = create_turtle(-50,50,"blue")
t4 = create_turtle(-50,-50,"lime")


def on_turtle_click(t):
    global clicks, clickLabel
    clicks += 1
    clickLabel.clear()
    clickLabel.write(f"Кліки: {clicks}", font=("Arial", 16, "normal"))
    t.left(90)


def on_t1_click(x, y):
    on_turtle_click(t1)


def on_t2_click(x, y):
    on_turtle_click(t2)


def on_t3_click(x, y):
    on_turtle_click(t3)


def on_t4_click(x, y):
    on_turtle_click(t4)


t1.onclick(on_t1_click)
t2.onclick(on_t2_click)
t3.onclick(on_t3_click)
t4.onclick(on_t4_click)


turtles = [t1, t2, t3, t4]


# ігровий цикл
while True:
    for t in turtles:
        t.forward(randint(0,5))
        if not is_turtle_inside(t):
            turtles_outside += 1
            turtlesLabel.clear()
            turtlesLabel.write(f"Втечі: {turtles_outside}", font=("Arial", 16, "normal"))
            turtles.remove(t)


    if clicks >= 4 or turtles_outside >= 4:
        break


# виведення інформації про результат гри
t1.clear()
t2.clear()
t3.clear()
t4.clear()


go_xy(getpen(), -50, 0)


if turtles_outside >= 4:
    color("red")
    write("Черепашки перемогли!", font=("Arial", 16, "normal"))
else:
    color("green")
    write("Учень переміг!", font=("Arial", 16, "normal"))

done()

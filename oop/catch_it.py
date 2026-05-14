from turtle import *
from random import randint, choice


screen = getscreen()
screen.bgcolor("black")
# screen.tracer(0)
speed(0)
hideturtle()


# функції для роботи програми
def go_xy(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# створення
def create_platform(x, y, cl):
    t = Turtle()
    t.speed(0)
    t.color(cl)
    t.shape("square")
    t.penup()
    t.goto(x, y)
    return t


# позначка, показує результат (скільки кліків і скільки черепашок втекли)
def create_label(x,y, cl, text):
    t = Turtle()
    t.speed(0)
    go_xy(t, x, y)
    t.color(cl)
    t.write(text, font=("Arial", 16, "normal"))
    t.hideturtle()
    return t


def create_field():
    color("#FFFFFF")
    go_xy(getpen(), -200, -200)
    begin_fill()
    for i in range(4):
        forward(400)
        left(90)
    end_fill()




def is_collide(t1, t2):
    dif_x = abs(t1.xcor() - t2.xcor())
    dif_y = abs(t1.ycor() - t2.ycor())
   
    if dif_x <= 10 and dif_y <= 10:
        return True


    return False


def create_apple():
    apple = Turtle()
    apple.color(choice(["red", "green", "yellow"]))
    apple.speed(0)
    apple.penup()
    apple.goto(randint(-200, 200), 160)
    apple.shape("circle")
    apple.setheading(-90)
    return apple


#######################################
# створення та налаштування ігрових об'єктів
apples = []
loop_counter = 0


score = 0
missed = 0
game = True




create_field()
missedLabel = create_label(-180, 180, "red", f"Пропущено: {missed}")
scoreLabel = create_label(30, 180, "green", f"Зібрано: {score}")


platform = create_platform(0, -180, "green")
def move_right():
    new_coord =  platform.xcor() + 20
    platform.goto(new_coord, -180)


def move_left():
    new_coord =  platform.xcor() - 20
    platform.goto(new_coord, -180)




def remove_apple(apple):
    apple.clear()
    apple.hideturtle()
    apples.remove(apple)

screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.listen()

def end_game(victory):
    global score
    platform.hideturtle()
    info = Turtle()
    info.penup()
    info.goto(-175, 0)
    if victory:
        info.color("green")
        info.write("Перемога", font=("Arial", 52, "normal"))
    else:
        info.color("red")
        info.write("Програш", font=("Arial", 64, "normal"))


def game_update():
    global score, missed, loop_counter


    for apple in apples:
        apple.forward(2)


        if is_collide(apple, platform):
            score+=1
            scoreLabel.clear()
            scoreLabel.write(f"Зібрано: {score}", font=("Arial", 16, "normal"))
            remove_apple(apple)
            if score == 2:
                end_game(True)
                return
               


        if apple.ycor() < -200:
            missed += 1
            missedLabel.clear()
            missedLabel.write(f"Пропущено: {missed}", font=("Arial", 16, "normal"))
            remove_apple(apple)
            if missed == 2:
                end_game(False)
                return

    loop_counter += 1
    if loop_counter > 80:
        apples.append(create_apple())
        loop_counter = 0


    # screen.update()
    screen.ontimer(game_update, 20)


game_update()


done()



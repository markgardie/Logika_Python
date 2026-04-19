import turtle
import random
import math

# екран
screen = turtle.Screen()
screen.title("Лови черепашок!")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)
screen.tracer(0)

score = 0

# текст
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)

def update_text():
    pen.clear()
    pen.write(f"Очки: {score}", align="center", font=("Arial", 16, "bold"))

update_text()

turtles = []

def get_speed_and_color(speed_type):
    if speed_type == "slow":
        return random.uniform(0.5, 1.5), "green", 50
    elif speed_type == "medium":
        return random.uniform(1.5, 3), "yellow", 100
    else:
        return random.uniform(3, 4.5), "red", 150


def create_turtle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()

    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    t.goto(x, y)

    # визначаємо ТІЛЬКИ при спавні
    speed_type = random.choice(["slow", "medium", "fast"])
    speed, color, reward = get_speed_and_color(speed_type)

    angle = random.uniform(0, 2 * math.pi)
    dx = math.cos(angle) * speed
    dy = math.sin(angle) * speed

    t.color(color)
   

    obj = {
        "t": t,
        "dx": dx,
        "dy": dy,
        "reward": reward,
        "speed_type": speed_type
    }

    def on_click(x, y):
        global score

        # додаємо очки
        score += obj["reward"]
        update_text()

        # тільки зміна руху (БЕЗ зміни кольору)
        speed, _, _ = get_speed_and_color(obj["speed_type"])

        angle = random.uniform(0, 2 * math.pi)
        obj["dx"] = math.cos(angle) * speed
        obj["dy"] = math.sin(angle) * speed

    t.onclick(on_click)

    return obj


# старт
for _ in range(3):
    turtles.append(create_turtle())


def game_loop():
    global score

    screen.update()

    for obj in turtles[:]:
        t = obj["t"]

        t.goto(t.xcor() + obj["dx"], t.ycor() + obj["dy"])

        # втекла → штраф + новий spawn
        if abs(t.xcor()) > 400 or abs(t.ycor()) > 300:
            t.hideturtle()
            turtles.remove(obj)

            score -= 50
            update_text()

    # підтримуємо кількість (нові = новий колір)
    while len(turtles) < 3:
        turtles.append(create_turtle())

    screen.ontimer(game_loop, 20)


game_loop()
screen.mainloop()
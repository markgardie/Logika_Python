import turtle 
import random 
 
# екран 
screen = turtle.Screen() 
screen.title("Лови черепашок!") 
screen.bgcolor("lightblue") 
screen.setup(width=800, height=600) 
screen.tracer(0) 
 
score = 0 
lives = 3 
 
# текст 
pen = turtle.Turtle() 
pen.hideturtle() 
pen.penup() 
pen.goto(0, 260) 
 
def update_text(): 
    pen.clear() 
    pen.write(f"Очки: {score}   Життя: {lives}", align="center", font=("Arial", 16, "bold")) 
 
update_text() 
 
turtles = [] 
 
def create_turtle(): 
    t = turtle.Turtle() 
    t.shape("turtle") 
    t.penup() 
 
    x = random.randint(-380, 380) 
    y = random.randint(-280, 280) 
    t.goto(x, y) 
 
    # швидкість + колір + trail 
    speed_type = random.choice(["slow", "medium", "fast"]) 
 
    if speed_type == "slow": 
        dx = random.uniform(-1, 1) 
        dy = random.uniform(-1, 1) 
        color = "green" 
    elif speed_type == "medium": 
        dx = random.uniform(-2.5, 2.5) 
        dy = random.uniform(-2.5, 2.5) 
        color = "yellow" 
    else: 
        dx = random.uniform(-4, 4) 
        dy = random.uniform(-4, 4) 
        color = "red" 
 
    t.color(color) 
    t.pendown()  # малює слід 
 
    #  КІЛЬКІСТЬ КЛІКІВ ЗАЛЕЖИТЬ ВІД КРАЮ 
    dist_edge = min(400 - abs(x), 300 - abs(y)) 
    max_clicks = int(max(3, dist_edge / 40))  # чим ближче — тим менше 
 
    obj = { 
        "t": t, 
        "dx": dx, 
        "dy": dy, 
        "clicks": 0, 
        "max_clicks": max_clicks 
    } 
 
    def on_click(x, y): 
        global score 
 
        obj["clicks"] += 1 
 
        #  змінює напрямок 
        obj["dx"] = random.uniform(-4, 4) 
        obj["dy"] = random.uniform(-4, 4) 
 
        if obj["clicks"] >= obj["max_clicks"]: 
            t.hideturtle() 
            if obj in turtles: 
                turtles.remove(obj) 
            score += 100 
            update_text() 
 
    t.onclick(on_click) 
 
    return obj 
 
# старт 
for _ in range(3): 
    turtles.append(create_turtle()) 
 
def game_loop(): 
    global lives 
 
    screen.update() 
 
    for obj in turtles[:]: 
        t = obj["t"] 
 
        t.goto(t.xcor() + obj["dx"], t.ycor() + obj["dy"]) 
 
        # втекла 
        if abs(t.xcor()) > 400 or abs(t.ycor()) > 300: 
            t.hideturtle() 
            turtles.remove(obj) 
            lives -= 1 
            update_text() 
 
    # нові 
    while len(turtles) < 3: 
        turtles.append(create_turtle()) 
 
    # програш 
    if lives <= 0: 
        pen.goto(0, 0) 
        pen.write("ТИ ПРОГРАВ!", align="center", font=("Arial", 24, "bold")) 
        return 
 
    screen.ontimer(game_loop, 20) 
 
game_loop() 
screen.mainloop()
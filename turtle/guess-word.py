from turtle import *
from art import *   
from random import randint

## Список кольорів пелюсток
colors = ["#c0392b", "#8e44ad", "#2471a3", "#138d75", "#f1c40f","#e74c3c","#5dade2"]

# координати квітки
x_start,y_start = -400,-150
# координати завдання
x_ask,y_ask = -170,100
# координати для відображення невірних літер
x_wrong, y_wrong = -170, 50

# радіус пелюстки та листочків
r = 95
# стартовий кут для пелюсток квітки
starting_angle = 360/7

# лічильники вірних та невірних слів
count_right = 0
count_wrong = 0

speed(0)
# список слів для гри
words = ["python", "turtle", "game", "flower", "color", "computer", "program"]
# випадкове слово для старту гри
word = words[randint(0, len(words)-1)]

# Функція для малювання однієї пелюстки
def draw_petal(col, radius):
    color(col)
    begin_fill()
    circle(radius, 60)  # Півколо
    left(120)  # Поворот для іншої сторони
    circle(radius, 60)  # Півколо
    left(120)  # Повернення в початкову позицію
    end_fill()

def draw_stem():
    start(x_start,y_start)
    setheading(90)
    color("green")
    width(20)
    fd(50)
    setheading(135)
    draw_petal("green",100)
    setheading(25)
    draw_petal("green",65)
    setheading(90)
    fd(150)
   
def draw_petals():    
    # Малювання квітки
    width(20)
    k = starting_angle
    for i in range(7):
        start(x_start, y_start + 200)
        setheading(k)
        draw_petal(colors[i], r)
        k += starting_angle
       
def draw_down_petal(col):
    draw_flower()
    xd = randint(x_start-50, x_start+50)
    start(xd, y_start)
    h = randint(180,360)
    setheading(h)
    width(20)
    draw_petal(col, r)
       
def draw_flower():
    draw_stem()
    draw_petals()

def write_ask(word):
    start(-170, 100)
    setheading(0)
    width(4)
    color("black")
    for w in word:
        fd(30)
        penup()
        fd(15)
        pendown()

def write_wrong(letter):
    color("black")
    write(letter, font=("Arial",28))
    color("red")
    width(2)
    setheading(45)
    fd(30)
    setheading(180)
    penup()
    fd(20)
    setheading(270+45)
    pendown()
    fd(30)
    color("grey")

def write_right(letter):
    start(-170, 105)
    penup()
    color("black")
    setheading(0)
    count = 0
    for w in word:
        if w == letter:
            pendown()
            write(letter,font=("Arial",32))
            penup()
            count += 1
        fd(45)
    return count

def end_game(col,txt):
    start(-50,-50)
    color(col)
    write(txt, font=("Arial",50))  # Виправлено "Arila" на "Arial"
 
# малюємо завдання
write_ask(word)
# малюємо квітку
draw_flower()

# ігровий цикл
while True:
    # запитуємо літеру у гравця
    letter = input("Введіть літеру:")
    # перевіряємо чи є така літера у слові
    if letter in word:
        # малюємо вірну літеру ТА рахуємо її кількість у слові
        c = write_right(letter)
        # збільшуємо лічильник вірних літер
        count_right += c
    # якщо літери немає у слові    
    else:
        # малюємо невірну літеру
        start(x_wrong,y_wrong)
        x_wrong += 45  # Виправлено x_Wrong на x_wrong
        write_wrong(letter)
        # збільшуємо лічильник невірних літер
        count_wrong += 1
        # ЗАПАМ'ЯТАТИ колір пелюстки
        col = colors[count_wrong-1]
        # ЗАМІНИТИ цей колір на білий
        colors[count_wrong-1] = "white"
        # малюємо квітку заново та впавшу пелюстку
        draw_down_petal(col)
       
    # перевірка програшу    
    if count_wrong == 7:
        end_game("red","Ти програв :(")
        break
    # перевірка виграшу
    if count_right == len(word):
        end_game("blue","Ти виграв!")
        break

# Залишаємо вікно відкритим до натискання миші
exitonclick()
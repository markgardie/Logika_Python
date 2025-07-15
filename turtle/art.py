from turtle import*

#функція квадрату за розміром та кольором
def square(a, col):
  color(col)
  for i in range(4):
    fd(a)
    lt(90)

#⭐функція квадрату за розміром,товщиною лінії та кольором
def square3(a,w, col):
  color(col)
  width(w)
  for i in range(4):
    fd(a)
    lt(90)
    
#⭐функція квадрату лише за розміром 
def square2(a):
  for i in range(4):
    fd(a)
    lt(90)

#функція прямокутника за розміром та кольором
def rectangle(a,b, col):
  color(col)
  for i in range(2):
    fd(a)
    lt(90)
    fd(b)
    lt(90)
    
#⭐функція прямокутника за розміром,товщиною лінії та кольором
def rectangle3(a,b,w, col):
  color(col)
  width(w)
  for i in range(2):
    fd(a)
    lt(90)
    fd(b)
    lt(90)

#⭐функція прямокутника лише за розміром 
def rectangle2(a,b):
  for i in range(2):
    fd(a)
    lt(90)
    fd(b)
    lt(90)

#функція трикутника за розміром та кольором
def triangle(a, col):
  color(col)
  for i in range(3):
    fd(a)
    lt(120)
    
#⭐функція трикутника за розміром, товщиною та кольором
def triangle3(a,w, col):
  color(col)
  width(w)
  for i in range(3):
    fd(a)
    lt(120)

#⭐функція трикутника лише за розміром
def triangle2(a):
  for i in range(3):
    fd(a)
    lt(120)

#функція паралелограма за розміром та кольором
def parallelogram(a, b, col):
  color(col)
  for i in range(2):
    fd(a)
    lt(125)
    fd(b)
    lt(55)
    
#⭐функція паралелограма за розміром, товщиною, кутом нахилу та кольором
def parallelogram3(a, b, w, angel, col):
  color(col)
  width(w)
  angel2 = 180 - angel
  for i in range(2):
    fd(a)
    lt(angel)
    fd(b)
    lt(angel2)

#⭐функція паралелограма лише за розміром та кутом нахилу 
def parallelogram2(a, b, angel):
  angel2 = 180 - angel
  for i in range(2):
    fd(a)
    lt(angel)
    fd(b)
    lt(angel2)
    
#функція багатокутника за розміром та кольором
def polygon(a, n, col):
  color(col)
  angel = 360 / n
  for i in range(n):
    fd(a)
    lt(angel)

#⭐функція багатокутника за розміром, товщиною та кольором
def polygon3(a, n, w, col):  # Змінено назву з polygon на polygon3
  color(col)
  width(w)
  angel = 360 / n
  for i in range(n):
    fd(a)
    lt(angel)

#⭐функція багатокутника лише за розміром
def polygon2(a, n):  # Додано відсутню функцію polygon2
  angel = 360 / n
  for i in range(n):
    fd(a)
    lt(angel)

#ЗАФАРБОВАНІ ФІГУРИ
#функція зафарбованого квадрату
def square_fill(a, col):
  color(col)
  begin_fill()
  for i in range(4):
    fd(a)
    lt(90)
  end_fill()

#функція зафарбованого прямокутника  
def rectangle_fill(a,b, col):
  color(col)
  begin_fill()
  for i in range(2):
    fd(a)
    lt(90)
    fd(b)
    lt(90)
  end_fill()

#функція зафарбованого трикутника
def triangle_fill(a, col):
  color(col)
  begin_fill()
  for i in range(3):
    fd(a)
    lt(120)
  end_fill()

#функція зафарбованого паралелограму
def parallelogram_fill(a, b, col):
  color(col)
  begin_fill()
  for i in range(2):
    fd(a)
    lt(125)
    fd(b)
    lt(55)
  end_fill()

#функція зафарбованого багатокутника
def polygon_fill(a, n, col):
  color(col)
  angel = 360 / n
  begin_fill()
  for i in range(n):
    fd(a)
    lt(angel)
  end_fill()

#функція зафарбованого кола
def circle_fill(a,col):
  color(col)
  begin_fill()
  circle(a)
  end_fill()

#функція зафарбованих фігур( ті самі), але з використанням попередньо написаних функцій фігур
def square_fill3(a, col):
  begin_fill()
  square(a,col)
  end_fill()
    
def rectangle_fill3(a,b, col):
  begin_fill()
  rectangle(a, b, col)
  end_fill()

def triangle_fill3(a, col):
  begin_fill()
  triangle(a, col)
  end_fill()

def parallelogram_fill3(a, b, col):
  begin_fill()
  parallelogram(a, b, col)
  end_fill()

def polygon_fill3(a, n, col):
  begin_fill()
  polygon(a, n, col)
  end_fill()

def circle_fill3(a,col):
  color(col)
  begin_fill()
  circle(a)
  end_fill()

#функція зафарбованих фігур( ті самі), але з використанням попередньо написаних функцій фігур БЕЗ вказання кольорів.КОЛЬОРИ будемо вказувати окремою функціює
def square_fill2(a):
  begin_fill()
  square2(a)
  end_fill()
    
def rectangle_fill2(a,b):
  begin_fill()
  rectangle2(a, b)
  end_fill()

def triangle_fill2(a):
  begin_fill()
  triangle2(a)  # Виправлено з triangle на triangle2
  end_fill()

def parallelogram_fill2(a, b, angel):  # Додано параметр angel
  begin_fill()
  parallelogram2(a, b, angel)
  end_fill()

def polygon_fill2(a, n):
  begin_fill()
  polygon2(a, n)
  end_fill()

def circle_fill2(a):
  begin_fill()
  circle(a)
  end_fill()

#функція старт - переміщення в координату
def start(x, y):
  penup()
  goto(x, y)
  pendown()
  
#функція старт лінії - встановлення кольору олівця, окремо кольору заливки та товщину лінії
def start_line(penCol, fillCol, w):
  pencolor(penCol)
  fillcolor(fillCol)
  width(w)

#функція фону
def fon(col1,col2):
  start(-350,100)
  width(400)
  color(col1)
  fd(900)
  
  start(-350,-150)
  width(250)
  color(col2)
  fd(900)
  
#функція зірки
def star(a, col):
  color(col)
  begin_fill()
  for i in range(5):
    fd(a)
    lt(144)
  end_fill()
  
#функція зірки з контуром
def star2(a, w,col1, col2):
  start_line(col1, col2, w)
  begin_fill()
  for i in range(5):
    fd(a)
    lt(144)
  end_fill()
  
#функція сонця
def sun(a, col ):
  color(col)
  begin_fill()
  for i in range(18):
    fd(a)
    lt(100)
  end_fill()
  
#функція сонця з контуром
def sun2(a, w, col1, col2):
  start_line(col1, col2, w)
  begin_fill()
  for i in range(18):
    fd(a)
    lt(100)
  end_fill()
  
#функція місяця
def moon(a,col1, col2):
  circle_fill(a, col1)
  lt(180) 
  penup()
  fd(a)
  pendown()
  rt(180)
  circle_fill(a, col2)
  
#функція градієнного фону
def gradient_fon(red, green, blue):
  width(20)
  x, y = -400, 200
  for i in range(25):
    color(red, green, blue)  # Виправлено формат rgb
    start(x, y)
    fd(800)
    blue -= 5 
    y -= 18

#функція куба
def coube(a, w, col1, col2):
  start_line(col1, col2, w)  # Виправлено порядок параметрів
  square_fill2(a)
  lt(90)
  fd(a)
  rt(90)
  parallelogram_fill2(a,a,30)
  fd(a)
  rt(90)
  parallelogram_fill2(a,a,120)
  
#функція сузір'я
def constellation(a, col):
  star(a, col)
  penup()
  setheading(110)
  fd(a)
  pendown()
  
  star(a, col)
  penup()
  setheading(20)
  fd(a)
  pendown()
  star(a, col)
  
  penup()
  setheading(295)
  fd(a)
  pendown()
  star(a, col)
  
  penup()
  setheading(285)
  fd(a)
  pendown()
  star(a, col)
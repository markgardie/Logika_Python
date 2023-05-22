from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import operator

from MainWindow import Ui_MainWindow

# Станий калькулятора
READY = 0
INPUT = 1


class Calculator(QMainWindow, Ui_MainWindow):

    # *args - змінна, яка дозволяє передавати у функцію будь-яку кількість НЕІМЕНОВАНИХ параметрів
    # **kwargs - змінна, яка дозволяє передавати у функцію будь-яку кількість ІМЕНОВАНИХ параметрів
    # Приклад:
    # Неіменовані параметри: print("hello"). Неіменований параметр - це просто значення
    # Іменовані параметри: print(text = "hello"). Іменований параметр - це пара ключ (назва) - значення
    def __init__(self, *args, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)

        # Налаштовуємо вікно
        self.setupUi(self)

        # Виставляємо слухачів кліку (подія pressed) для всіх цифрових кнопок
        # Проходимось циклом від 0 до 10 (невключно, тобто до 9)
        # Ці цифри підставляються у n в фігурних дужках
        # При виникненні події кліка, запускаємо (connect) функцію input_number
        # В функцію треба передати параметр, цифру, тому для цього використовуємо лямбду
        # Лямбда - це анонімна функція, тобто функція без назви
        for n in range(0, 10):
            getattr(self, f'pushButton_n{n}').pressed.connect(lambda v=n: self.input_number(v))

        # Виставляємо слухачів клікі для арифметичних операцій
        # При натисканні на кнопку операція запускається функція operation
        # Ця функція приймає параметром іншу функцію
        # В даному випадку ми передаємо функцію add, sub, mul, truediv, функція, які виконують арифметичні операції
        self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
        self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
        self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
        self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv)) 

        # Виставляємо слухачів для кнопки знаходження відсотка та дорівнює
        self.pushButton_pc.pressed.connect(self.operation_pc)
        self.pushButton_eq.pressed.connect(self.equals)

        # Виставляємо слухача кліка на кнопку очищення AC
        # Додатково виставляємо слухача натискання на клавішу (triggered)
        # Тобто очистити калькулятор можна або кліком мишкою по кнопці AC (подія pressed)
        # Або натискання певної клавіші на клавіатурі (подія triggered)
        self.actionReset.triggered.connect(self.reset)
        self.pushButton_ac.pressed.connect(self.reset)

        # Слухач клавіатури для закриття калькулятора
        self.actionExit.triggered.connect(self.close)

        # Слухачі кліків на кнопки роботи із пам'яттю M, MR
        self.pushButton_m.pressed.connect(self.memory_store)
        self.pushButton_mr.pressed.connect(self.memory_recall)

        # При запуску калькулятора в пам'яті нічого немає
        self.memory = 0
        # Також при запуску, очищуємо калькулятор
        self.reset()

        # Показуємо вікно калькулятора
        self.show()

    # функція для показу чисел на екрані
    def display(self):
        # показуємо на LCD екрані останню цифру в стеку (-1)
        self.lcdNumber.display(self.stack[-1])

    # функція для обнулення калькулятора
    def reset(self):
        # змінюємо стан на початковий
        self.state = READY
        # обнуляємо цифри в стеку
        self.stack = [0]
        # останньої та поточної операції немає
        self.last_operation = None
        self.current_op = None
        # показуємо на екрані цифру 0
        self.display()

    # функція для збереження числа в пам'ять
    def memory_store(self):
        # записуємо в пам'яті цифру, яка знаходиться на LCD екрані
        self.memory = self.lcdNumber.value()

    # функція для отримання числа із пам'яті
    def memory_recall(self):
        # змінюємо на стан вводу (було вже щось введено)
        self.state = INPUT
        # дістаємо з пам'яті цифру і додаємо в кінець (-1) стеку
        self.stack[-1] = self.memory
        # показуємо цифри на екрані
        self.display()

    # функція для введення цифр
    def input_number(self, v):
        # якщо початковий стан
        if self.state == READY:
            # змінюємо стан на стан вводу, бо було вже введено цифру
            self.state = INPUT
            # додаємо введену цифру в стек
            self.stack[-1] = v
        else:
            # якщо вже було введено певну цифру
            # множимо цю введену цифру на 10, аби збільшити розряд
            # наприклад одиниці перетворити в десятки, десятки в сотні і т.д.
            self.stack[-1] = self.stack[-1] * 10 + v
        
        # показуємо цифру на екрані
        self.display()

    # функція для запуску арифметичних операцій
    def operation(self, op):
        # якщо до поточної операції була незавершена попередня операція
        if self.current_op:  
            # запускаємо розрахунок попередньою операції
            self.equals()

        # додаємо в стек 0
        self.stack.append(0)
        # змінюємо стан, бо була введене операція
        self.state = INPUT
        # записуємо введену операцію в поточну
        self.current_op = op

    # функція для розрахунку відсотків
    def operation_pc(self):
        # змінюємо стан, бо була введене операція знаходження відсотків 
        self.state = INPUT
        # для знаходження відсотків беремо останні елемент в стеку і множимо на 0.01 (замість ділення на 100)
        self.stack[-1] *= 0.01
        # показуємо результат на екрані
        self.display()

    def equals(self):
        
        # ця умова дозволяємо натисканням на "=" знову повторити попередню операцію
        # наприклад, в останній операції ми додавали 3
        # натискаючи постійно на "=" ми будемо постійно повторювати це додавання
        # умова: якщо початковий стан і є остання операція
        if self.state == READY and self.last_operation:
            # цю останню операцію робимо поточною, яку треба виконати
            s, self.current_op = self.last_operation
            # додаємо число в стек
            self.stack.append(s)

        # якщо була введена якась операція
        if self.current_op:
            # записуємо в останню операцію (для можливості повторення через "=")
            self.last_operation = self.stack[-1], self.current_op

            try:
                # намагаємось виконати операцію з числами в стеку
                self.stack = [self.current_op(*self.stack)]
            except Exception:
                # якщо виникаємо виключення
                # то показуємо на екрані помилку
                self.lcdNumber.display('Err')
                # обнуляємо стек
                self.stack = [0]
            else:
                # після операції вказуємо, що операції немає
                self.current_op = None
                # повертає стан до початкового
                self.state = READY
                # показуємо на екрані цифри
                self.display()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculon")

    calc = Calculator()
    app.exec_()
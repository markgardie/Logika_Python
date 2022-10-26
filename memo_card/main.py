from app import app
from layout.question_layout import (
   mainColumn, app,
   questionLabel, correctAnswerLabel, resultLabel,
   ansRadioButton1, ansRadioButton2, ansRadioButton3, ansRadioButton4,
   answerButton, questionWindow
)
from functions import showQuestion, showResult, showData, clickOK
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle # будем перемешивать ответы в карточке вопроса
from constants import*


#Створити список радіо-кнопок відповідей
ansList = [ansRadioButton1, ansRadioButton2, ansRadioButton3, ansRadioButton4]

#Перемішати їх
shuffle(ansList)


#Визначаємо перший елемент як правильну відповідь
answer = ansList[0]
wrongAnswer1 = ansList[1]
wrongAnswer2 = ansList[2]
wrongAnswer3 = ansList[3]

#Запускаємо функцію показу даних
showData(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3)

#Запускаємо функцію показу питання
showQuestion()

#Прописуємо підписку на подію кліку по кнопці "Відповісти"
answerButton.clicked.connect(lambda: clickOK())

#Показати вікно питання
questionWindow.show()

#Запустити додаток
app.exec_()
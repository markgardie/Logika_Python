from app import app
from layout.question_layout import (
   mainColumn, app,
   questionLabel, correctAnswerLabel, resultLabel,
   ansButton1, ansButton2, ansButton3, ansButton4,
   answerButton
)
from functions import showQuestion, showResult, showData, clickOK
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle # будем перемешивать ответы в карточке вопроса
from constants import*



#Створити список радіо-кнопок відповідей
#Перемішати їх
#Визначаємо перший елемент як правильну відповідь
#Запускаємо функцію показу даних
#Запускаємо функцію показу питання
#Прописуємо підписку на подію кліку по кнопці "Відповісти"
answerButton.clicked.connect(lambda: clickOK())

#Показати вікно питання
#Запустити додаток
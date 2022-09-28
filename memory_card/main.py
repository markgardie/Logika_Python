from card_layout import (
   mainColumn, app,
   questionLabel, correctAnswerLabel, resultLabel,
   ansButton1, ansButton2, ansButton3, ansButton4,
   answerButton
)
from show_functions import showQuestion, showResult, showData, clickOK
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle # будем перемешивать ответы в карточке вопроса
from constants import*


 
# Теперь нам нужно показать эти данные,
# причём ответы распределить случайно между радиокнопками, и помнить кнопку с правильным ответом.
# Для этого создадим набор ссылок на радиокнопки и перемешаем его
ansList = [ansButton1, ansButton2, ansButton3, ansButton4]
shuffle(ansList)
answer = ansList[0] # мы не знаем, какой это из радиобаттонов, но можем положить сюда правильный ответ и запомнить это
wrongAnswer1, wrongAnswer2, wrongAnswer3 = ansList[1], ansList[2], ansList[3]
 
winCard = QWidget()
winCard.resize(CARD_WIDTH, CARD_HEIGHT)
winCard.move(WINDOW_X, WINDOW_Y)
winCard.setWindowTitle('Memory Card')
 
winCard.setLayout(mainColumn)
showData(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3)
showQuestion()
answerButton.clicked.connect(lambda: clickOK(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3))
 
winCard.show()
app.exec_()

from app import app
from layouts.question_layout import questionWindow, timerButton
from functions import *
from random import shuffle # будем перемешивать ответы в карточке вопроса


ansList = [ansRadioButton1, ansRadioButton2, ansRadioButton3, ansRadioButton4]
shuffle(ansList)
answer = ansList[0] # мы не знаем, какой это из радиобаттонов, но можем положить сюда правильный ответ и запомнить это
wrongAnswer1, wrongAnswer2, wrongAnswer3 = ansList[1], ansList[2], ansList[3]


showData(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3)
showQuestion()

answerButton.clicked.connect(lambda: clickOK(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3))
timerButton.clicked.connect(clickRest)

questionWindow.show()
app.exec_()
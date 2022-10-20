from layouts.question_layout import (
    resultGroupBox, ansGroupBox, answerButton,
    ansButtonGroup, ansRadioButton1, ansRadioButton2, minutesLabel,
    ansRadioButton3, ansRadioButton4, questionLabel, timer, timerButton
) 
from layouts.result_layout import correctAnswerLabel, resultLabel
from layouts.rest_layout import timerLabel, restGroupBox
from constants import*
from PyQt5.QtCore import QTimer, QTime


def showQuestion():
    resultGroupBox.hide()
    ansGroupBox.show()

    answerButton.setText('Відповісти')

    ansButtonGroup.setExclusive(False)
    
    ansRadioButton1.setChecked(False)
    ansRadioButton2.setChecked(False)
    ansRadioButton3.setChecked(False)
    ansRadioButton4.setChecked(False)

    ansButtonGroup.setExclusive(True)


def showResult():
   ''' показать панель ответов '''
   ansGroupBox.hide()
   resultGroupBox.show()
   answerButton.setText('Спробувати ще раз')

def showData(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
   ''' показывает на экране нужную информацию '''
   # объединим в функцию похожие действия
   questionLabel.setText(QUESTION_TEXT)
   correctAnswerLabel.setText(RIGHT_TEXT)
   answer.setText(RIGHT_TEXT)
   wrongAnswer1.setText(WRONG_TEXT1)
   wrongAnswer2.setText(WRONG_TEXT2)
   wrongAnswer3.setText(WRONG_TEXT3)
 

def checkAnswer(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
    correct = answer.isChecked()

    if correct:
        resultLabel.setText(TEXT_CORRECT)
    else:
        resultLabel.setText(TEXT_WRONG)

    showResult()
    


def clickOK(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
    if answerButton.text() != 'Спробувати ще раз':
        checkAnswer(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3)
    else:
        showQuestion()

def showMainWidgets():

    restGroupBox.hide()

    questionLabel.show()
    answerButton.show()
    timer.show()
    timerButton.show()
    minutesLabel.show()

    showQuestion()

    
def showRest():
    ansGroupBox.hide()
    questionLabel.hide()
    answerButton.hide()
    timer.hide()
    timerButton.hide()
    minutesLabel.hide()

    restGroupBox.show()
    

def clickRest():
    
    sleepTimer = QTimer()
    sleepTime = QTime()

    showRest()


    timerLabel.setText(f"Відпочиваємо {timer.value()} хвилин")

    sleepTimer.timeout.connect(showMainWidgets)
    sleepTimer.start(60)
    
    
    


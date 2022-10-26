from layout.question_layout import*
from layout.result_layout import*
from layout.timer_layout import*
from constants import*
from PyQt5.QtCore import QTimer, QTime

def showQuestion():
    resultGroupBox.hide()
    ansGroupBox.show()

    ansButtonGroup.setExclusive(False)
    
    ansRadioButton1.setChecked(False)
    ansRadioButton2.setChecked(False)
    ansRadioButton3.setChecked(False)
    ansRadioButton4.setChecked(False)

    ansButtonGroup.setExclusive(True)


#Функція перевірки результату (чи правильно відповіли)
def checkAnswer(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
    correct = answer.isChecked()

    if correct:
        resultLabel.setText(TEXT_CORRECT)
    else:
        resultLabel.setText(TEXT_WRONG)

    showResult()
    

#Функція-обробник кліка
def clickOK(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
    if answerButton.text() != 'Наступне питання':
        checkAnswer(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3)

#Функція показу результату
def showResult():
   ''' показать панель ответов '''
   ansGroupBox.hide()
   resultGroupBox.show()
   answerButton.setText('Спробувати ще раз')

#Функція показу даних
def showData(answer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
   ''' показывает на экране нужную информацию '''
   # объединим в функцию похожие действия
   questionLabel.setText(QUESTION_TEXT)
   correctAnswerLabel.setText(RIGHT_TEXT)
   answer.setText(RIGHT_TEXT)
   wrongAnswer1.setText(WRONG_TEXT1)
   wrongAnswer2.setText(WRONG_TEXT2)
   wrongAnswer3.setText(WRONG_TEXT3)


def showMainWidgets():

    timerGroupBox.hide()

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

    timerGroupBox.show()
    

def clickRest():
    
    sleepTimer = QTimer()

    showRest()

   
    timerLabel.setText(f"Відпочиваємо {timer.value()} хвилин")

    sleepTimer.timeout.connect(showMainWidgets)
    sleepTimer.start(60)
    

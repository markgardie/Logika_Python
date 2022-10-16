from layout.question_layout import*
from constants import*

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
#Функція показу даних


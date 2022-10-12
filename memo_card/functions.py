from layout import*
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


#Функція показу результату
#Функція показу даних
#Функція перевірки результату (чи правильно відповіли)
#Функція-обробник кліка

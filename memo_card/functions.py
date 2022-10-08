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

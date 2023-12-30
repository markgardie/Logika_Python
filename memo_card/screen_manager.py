from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from edit_screen import EditScreen
from question_screen import QuestionScreen
from question import Question

Q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
Q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
Q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
Q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

QUESTIONS = [Q1, Q2, Q3, Q4]

class ScreenManager():

    def __init__(self):

        self.questionScreen = QuestionScreen()

        self.radioAnswers = [
            self.questionScreen.ansButton1,
            self.questionScreen.ansButton2,
            self.questionScreen.ansButton3,
            self.questionScreen.ansButton4,
        ]

    def setListeners(self):
        pass
    
    def checkAnswer(self):
        self.questionScreen.radioGroup.setExclusive(False)

        # перевірка відповіді

        self.questionScreen.radioGroup.setExclusive(True)

    def clickOk(self):
        pass
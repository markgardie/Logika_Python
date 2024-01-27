from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from edit_screen import EditScreen
from question_screen import QuestionScreen
from question import Question
from random import choice, shuffle
from time import sleep

Q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
Q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
Q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
Q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [Q1, Q2, Q3, Q4]

class ScreenManager():

    def __init__(self):

        self.questionScreen = QuestionScreen()

        self.radioAnswers = [
            self.questionScreen.ansButton1,
            self.questionScreen.ansButton2,
            self.questionScreen.ansButton3,
            self.questionScreen.ansButton4,
        ]

        self.setNewQuestion()

    def setListeners(self):
        self.екран.кнопка.clicked.connect(функція)
    
    
    def setNewQuestion(self):
        self.currentQuestion = choice(questions)

        self.questionScreen.questionLabel.setText(self.currentQuestion.question)
        self.questionScreen.rightAnswerLabel.setText(self.currentQuestion.rightAnswer)

        shuffle(self.radioAnswers)

        self.radioAnswers[0].setText(self.currentQuestion.wrongAnswer1)
        self.radioAnswers[1].setText(self.currentQuestion.wrongAnswer2)
        self.radioAnswers[2].setText(self.currentQuestion.wrongAnswer3)
        self.radioAnswers[3].setText(self.currentQuestion.rightAnswer)

    
    def checkAnswer(self):
        self.questionScreen.radioGroup.setExclusive(False)

        for ansButton in self.radioAnswers:
            if ansButton.isChecked():
                if ansButton.text() == self.questionScreen.rightAnswerLabel.text():
                    self.currentQuestion.gotRight()
                    self.questionScreen.resultLabel.setText("Правильно")
                    ansButton.setChecked(False)
                    break

        else:
            self.currentQuestion.gotWrong()
            self.questionScreen.resultLabel.setText("Не правильно")


        self.questionScreen.radioGroup.setExclusive(True)

    def clickOk(self):
        
        if self.questionScreen.nextButton.text() == "Відповісти":
            self.checkAnswer()

            self.questionScreen.questionGroupBox.hide()
            self.questionScreen.answerGroupBox.show()

            self.questionScreen.nextButton.setText("Наступне питання")
        else:
            self.setNewQuestion()

            self.questionScreen.questionGroupBox.show()
            self.questionScreen.answerGroupBox.hide()

            self.questionScreen.nextButton.setText("Відповісти")

    def clearEdits(self):
        self.editScreen.questionEdit.clear()
        self.editScreen.rightEdit.clear()
        self.editScreen.wrongEdit1.clear()
        self.editScreen.wrongEdit2.clear()
        self.editScreen.wrongEdit3.clear()

    def addQuestion(self):
        newQuestion = Question(
            self.editScreen.questionEdit.text(),
            self.editScreen.rightEdit.text(),
            self.editScreen.wrongEdit1.text(),
            self.editScreen.wrongEdit2.text(),
            self.editScreen.wrongEdit3.text()
        )

        questions.append(newQuestion)

        self.clearEdits()


    def generateStats(self):
        if self.currentQuestion.countAsk == 0:
            rate = 0
        else:
            rate = self.currentQuestion.countRight / self.currentQuestion.countAsk * 100
        

        all_text = f"Разів відповіли: {self.currentQuestion.countAsk} \n" 
        right_text = f"Вірних відповідей: {self.currentQuestion.countRight} \n" 
        rate_text = f"Успішність: {round(rate, 2)} \n" 

        self.editScreen.statsLabel.setText(all_text + right_text + rate_text)

    def rest(self):
        self.questionScreen.hide()
        sleep(self.questionScreen.restSpinBox.value() * 60)
        self.questionScreen.show()

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
        self.editScreen = EditScreen()

        self.answers = [
            self.questionScreen.ansRadio1,
            self.questionScreen.ansRadio2,
            self.questionScreen.ansRadio3,
            self.questionScreen.ansRadio4
        ]

        self.setNewQuestion()
        self.questionScreen.show()

    def setListeners(self):
        pass
    
    
    def setNewQuestion(self):
        self.currentQuestion = choice(questions)

        self.questionScreen.questionLabel.setText(self.currentQuestion.question)
        self.questionScreen.rightAnswerLabel.setText(self.currentQuestion.rightAnswer)

        shuffle(self.answers)

        self.answers[0].setText(self.currentQuestion.rightAnswer)
        self.answers[1].setText(self.currentQuestion.wrongAnswer1)
        self.answers[2].setText(self.currentQuestion.wrongAnswer2)
        self.answers[3].setText(self.currentQuestion.wrongAnswer3)
    
    def checkAnswer(self):
        for radio in self.answers:
            if radio.isChecked():
                if radio.text() == self.currentQuestion.rightAnswer:
                    self.currentQuestion.gotRight()
                    self.questionScreen.resultLabel.setText("Правильно")
                    radio.setChecked(False)
                    break
        else:
            self.currentQuestion.gotWrong()
            self.questionScreen.resultLabel.setText("Не правильно")

    def clickOk(self):
        if self.questionScreen.okButton.text() == "Відповісти":
            self.checkAnswer()
            self.questionScreen.answerGroupBox.hide()
            self.questionScreen.resultGroupBox.show()
            self.questionScreen.okButton.setText("Наступне питання")
        else:
            self.setNewQuestion()
            self.questionScreen.answerGroupBox.show()
            self.questionScreen.resultGroupBox.hide()
            self.questionScreen.okButton.setText("Відповісти")

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
        sleep(self.questionScreen.minutesSpinBox.value() * 60)
        self.questionScreen.show()
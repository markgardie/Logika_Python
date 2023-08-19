from ui.QuestionScreen import QuestionScreen
from ui.ResultScreen import ResultScreen
from utils.Constants import*

class Navigation():

    def __init__(self):
        self.questionScreen = QuestionScreen(QUESTION_SCREEN_WIDTH, QUESTION_SCREEN_HEIGHT, TITLE)
        self.resultScreen = ResultScreen(QUESTION_SCREEN_WIDTH, QUESTION_SCREEN_HEIGHT, TITLE)

        self.right = False

        self.questionScreen.show()
        self.clickListeners()

    def clickListeners(self):
        self.questionScreen.ansRadioButton1.clicked.connect(self.setWin)
        self.questionScreen.ansRadioButton2.clicked.connect(self.setLose)
        self.questionScreen.ansRadioButton3.clicked.connect(self.setLose)
        self.questionScreen.ansRadioButton4.clicked.connect(self.setLose)

        self.questionScreen.answerButton.clicked.connect(self.navigateToResult)
        self.resultScreen.answerButton.clicked.connect(self.navigateToQuestion)


    def setWin(self): self.right = True

    def setLose(self): self.right = False

    def navigateToResult(self):
        self.resultScreen.putData(self.right, self.questionScreen.questionLabel.text)
        self.questionScreen.hide()
        self.resultScreen.show()

    def navigateToQuestion(self):
        self.questionScreen.show()
        self.resultScreen.hide()




from screens.QuestionScreen import QuestionScreen
from PyQt5.QtWidgets import QApplication
from utils.Constants import*

class MemoCardApp(QApplication):

    def __init__(self):
        super().__init__([])

        self.questionScreen = QuestionScreen(QUESTION_SCREEN_WIDTH, QUESTION_SCREEN_HEIGHT, TITLE)

app = MemoCardApp()
app.questionScreen.show()
app.exec_()
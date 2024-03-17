from random import randint

class MainController():

    def __init__(self):
        self.question_num = 0
        self.last_question = 0 

    def index(self):
        self.question_num = randint(0, 3)
        return '<a href="/quiz">Тест</a>'
    
    def quiz(self):
        return "This is quiz"
    
    def result(self):
        return "Quiz result"
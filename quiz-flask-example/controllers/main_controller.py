from random import randint

class MainController():

    def __init__(self):
        self.quiz = 0
        self.last_question = 0

    def index(self):
        self.quiz = randint(1, 3)
        return '<a href="/quiz">Тест</a>'
        
    def quiz(self):
        return "This is quiz"
        
    def result(self):
        return "Quiz result"
class Question():

    def __init__(self, question, rightAnswer, 
                 wrongAnswer1, wrongAnswer2, wrongAnswer3):
        
        self.question = question
        self.rightAnswer = rightAnswer
        self.wrongAnswer1 = wrongAnswer1
        self.wrongAnswer2 = wrongAnswer2
        self.wrongAnswer3 = wrongAnswer3

        
        self.isAnswer = False
        self.countAsk = 0
        self.countRight = 0

    def gotRight(self):
        self.countAsk += 1
        self.countRight += 1

    def gotWrong(self):
        self.countAsk += 1
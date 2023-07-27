from domain.Card import Card
from utils.Constants import*

class CardRepository():

    def __init__(self):

        startCard = Card(START_QUESTION, START_ANS1, START_ANS2, START_ANS3, START_ANS4)
        self.cardsList = [startCard]

    def addCard(self, question, rightAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
        questionModel = Card(question, rightAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3)
        self.cardsList.append(questionModel)

    def deleteCard(self, question):
        for card in self.cardsList:
            if (card.question == question):
                self.cardsList.remove(card)
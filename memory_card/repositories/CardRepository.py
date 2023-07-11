from models.Card import Card

class CardRepository():

    def __init__(self):

        self.cardsList = []

    def addCard(self, question, rightAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3):
        questionModel = Card(question, rightAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3)
        self.cardsList.append(questionModel)

    def deleteCard(self, question):
        for card in self.cardsList:
            if (card.question == question):
                self.cardsList.remove(card)
from domain.Card import Card

class Repository():

    def __init__(self):
        self.cardList = []

    def addCard(self, card):
        self.cardList.append(card)

    def deleteCard(self, card):
        self.cardList.remove(card)

    def readCard(self, cardNum):
        return self.cardList[cardNum]
    
    def updateCard(self, cardNum, newCard):
        self.cardList[cardNum] = newCard
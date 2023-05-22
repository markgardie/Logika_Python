class Piece:
	def __init__(self, color, king = False):
		self.color = color # колір шашки, червоний або синій
		self.king = king # чи являється шашка дамкою

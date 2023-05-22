
# Клас квадратного поля дошки
class Square:
	def __init__(self, color, busy = None):
		self.color = color # колір квадрата, або чорний, або білий
		self.busy = busy # чи зайняте поле шашкою
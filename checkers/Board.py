from Square import Square
from Piece import Piece
from constants import*


class Board:
	def __init__(self):
		self.matrix = self.new_board()

	# функція, яка створює нову дошку
	def new_board(self):
		"""
		Create a new board matrix.
		"""

		# спочатку створюється пуста матриця розмірами 8 на 8
		# матриця - це таблиця
		matrix = [[None] * 8 for i in range(8)]

		
		# проходимось по 8 стовпцям та 8 рядам
		for x in range(8):
			for y in range(8):
				# в залежності від парності координат (!= 0 означає непарне і навпаки)
				# створюємо поля різних кольорів
				# і заповнюємо матрицю
				if (x % 2 != 0) and (y % 2 == 0):
					matrix[y][x] = Square(WHITE)
				elif (x % 2 != 0) and (y % 2 != 0):
					matrix[y][x] = Square(BLACK)
				elif (x % 2 == 0) and (y % 2 != 0):
					matrix[y][x] = Square(WHITE)
				elif (x % 2 == 0) and (y % 2 == 0): 
					matrix[y][x] = Square(BLACK)

		# 8 стовпців
		for x in range(8):
			# для верхніх 3 рядів
			for y in range(3):
				# якщо поле чорне
				if matrix[x][y].color == BLACK:
					# створюємо на цьому полі червону шашку
					matrix[x][y].busy = Piece(RED)
			# 6, 7, 8 ряд
			for y in range(5, 8):
				if matrix[x][y].color == BLACK:
					# створюємо сині шашки
					matrix[x][y].busy = Piece(BLUE)

		return matrix

	def board_string(self, board):
		"""
		Takes a board and returns a matrix of the board space colors. Used for testing new_board()
		"""

		board_string = [[None] * 8] * 8 

		for x in range(8):
			for y in range(8):
				if board[x][y].color == WHITE:
					board_string[x][y] = "WHITE"
				else:
					board_string[x][y] = "BLACK"


		return board_string
	
	# функція, яка повертає координати поля, яке знаходиться в певному напрямку від початкого поля
	def rel(self, dir, coords):
		"""
		Returns the coordinates one square in a different direction to coords.
		===DOCTESTS===
		>>> board = Board()
		>>> board.rel(NORTHWEST, (1,2))
		(0,1)
		>>> board.rel(SOUTHEAST, (3,4))
		(4,5)
		>>> board.rel(NORTHEAST, (3,6))
		(4,5)
		>>> board.rel(SOUTHWEST, (2,5))
		(1,6)
		"""
		# координати початкового поля
		x, y = coords
		# якщо треба знайти поле вгорі злів
		if dir == NORTHWEST:
			# то х зменшується, а у збільшується
			return (x - 1, y - 1)
		elif dir == NORTHEAST:
			return (x + 1, y - 1)
		elif dir == SOUTHWEST:
			return (x - 1, y + 1)
		elif dir == SOUTHEAST:
			return (x + 1, y + 1)
		else:
			return 0

	# функція, повертає координати всіх діагональних суміжних квадратів
	def adjacent(self, coords):
		"""
		Returns a list of squares locations that are adjacent (on a diagonal) to coords.
		"""
		# тут 4 рази викликається функція rel
		# в усіх чотирьох напрямках
		return [self.rel(NORTHWEST, coords), self.rel(NORTHEAST, coords),self.rel(SOUTHWEST, coords),self.rel(SOUTHEAST, coords)]

	# функція, яка повертає поле за певними координатами
	def location(self, coords):
		"""
		Takes a set of coordinates as arguments and returns self.matrix[x][y]
		This can be faster than writing something like self.matrix[coords[0]][coords[1]]
		"""
		# координати
		x, y = coords

		# координати являються номерами в матриці, за якими можна отримати елементи (поле) в цій матриці
		return self.matrix[x][y]

	# функція, яка повертає координати полів, на які можна ходити
	# без урахування ворожих шашок, стрибка і т.д.
	def blind_legal_moves(self, coords):
		"""
		Returns a list of blind legal move locations from a set of coordinates coords on the board. 
		If that location is empty, then blind_legal_moves() return an empty list.
		"""
		x, y = coords

		# якщо на полі є шашка
		if self.matrix[x][y].busy != None:

			# якщо шашка не дамка і синя
			if self.matrix[x][y].busy.king == False and self.matrix[x][y].busy.color == BLUE:
				# можливими кроками являються північні напрямки
				blind_legal_moves = [self.rel(NORTHWEST, coords), self.rel(NORTHEAST, coords)]
			
			# якщо шашка не дамка і червона	
			elif self.matrix[x][y].busy.king == False and self.matrix[x][y].busy.color == RED:
				# можливими кроками являються південні напрямки
				blind_legal_moves = [self.rel(SOUTHWEST, coords), self.rel(SOUTHEAST, coords)]

			# якщо шашка являється дамкою
			else:
				# можливі всі 4 напрямки
				blind_legal_moves = [self.rel(NORTHWEST, coords), self.rel(NORTHEAST, coords), self.rel(SOUTHWEST, coords), self.rel(SOUTHEAST, coords)]

		# якщо на полі немає шашки
		else:
			# то і можливих кроків не існує
			blind_legal_moves = []

		return blind_legal_moves

	# можливі кроки з урахуванням шашок, які заважають, можливістю стрибка і т.д.
	def legal_moves(self, coords, hop = False):
		"""
		Returns a list of legal move locations from a given set of coordinates coords on the board.
		If that location is empty, then legal_moves() returns an empty list.
		"""
		x, y = coords

		blind_legal_moves = self.blind_legal_moves(coords) 
		legal_moves = []

		# якщо стрибок неможливий
		if hop == False:
			for move in blind_legal_moves:
				if hop == False:
					# перевіряємо, чи не зайшла шашка в глухий кут
					if self.on_board(move):
						# якщо в напрямку нашого ходу немає інших шашок
						if self.location(move).busy == None:
							# додаємо цей крок в список можливих хожів
							legal_moves.append(move)
						
						elif self.location(move).busy.color != self.location(coords).busy.color and self.on_board((move[0] + (move[0] - x), move[1] + (move[1] - y))) and self.location((move[0] + (move[0] - x), move[1] + (move[1] - y))).busy == None: # is this location filled by an enemy piece?
							legal_moves.append((move[0] + (move[0] - x), move[1] + (move[1] - y)))

		# якщо стрибок можливий
		else: 
			for move in blind_legal_moves:
				# перевіряємо чи не зайшли в глухий кут (on_board)
				# також перевіряємо чи заважає нашому ходу інша шашка
				if self.on_board(move) and self.location(move).busy != None:
					# якщо поле зайнято ворожою шашкою
					# і через цю шашку є пусте поле
					if self.location(move).busy.color != self.location(coords).busy.color and self.on_board((move[0] + (move[0] - x), move[1] + (move[1] - y))) and self.location((move[0] + (move[0] - x), move[1] + (move[1] - y))).busy == None: 
						# то ми додаємо можливий крок через стрибок
						legal_moves.append((move[0] + (move[0] - x), move[1] + (move[1] - y)))

		return legal_moves

	# функція для видалення шашки
	def remove_piece(self, coords):
		"""
		Removes a piece from the board at position coords. 
		"""
		x, y = coords
		# кажемо, що поле в певних координатах вже незайнято (None)
		self.matrix[x][y].busy = None

	# функція для руху шашок
	def move_piece(self, start_coords, end_coords):
		"""
		Move a piece from (start_x, start_y) to (end_x, end_y).
		"""
		# координати звідки рухаємось
		start_x, start_y = start_coords
		# координати, куди рухаємось
		end_x, end_y = end_coords

		# в поле в нових координатах копіюємо шашки із старих координат
		self.matrix[end_x][end_y].busy = self.matrix[start_x][start_y].busy
		# видаляємо шашку із старих координат
		self.remove_piece((start_x, start_y))

		# перевіряємо, чи стала шашка дамкою в нових координатах
		self.king((end_x, end_y))

	# функція, яка перевіряє, чи знаходиться поле в кінцевому ряді (для створення дамки)
	def is_end_square(self, coords):
		"""
		Is passed a coordinate tuple coords, and returns true or 
		false depending on if that square on the board is an end square.
		===DOCTESTS===
		>>> board = Board()
		>>> board.is_end_square((2,7))
		True
		>>> board.is_end_square((5,0))
		True
		>>>board.is_end_square((0,5))
		False
		"""

		# якщо це перший або восьмий ряд
		if coords[1] == 0 or coords[1] == 7:
			# то так, це ряд для створення дамки
			return True
		else:
			# інакше, це не ряд для створення дамки
			return False

	# функція, яка перевіряє, чи зайшли ми в глухий кут
	def on_board(self, coords):
		"""
		Checks to see if the given square coords lies on the board.
		If it does, then on_board() return True. Otherwise it returns false.
		===DOCTESTS===
		>>> board = Board()
		>>> board.on_board((5,0)):
		True
		>>> board.on_board(-2, 0):
		False
		>>> board.on_board(3, 9):
		False
		"""
		x, y = coords

		# якщо координати менше 1 і більше 8
		if x < 0 or y < 0 or x > 7 or y > 7:
			# то це не координати дошки
			# отже ми вийшли за межі дошки
			# і це глухий кут
			return False
		else:
			# інакше ми все ще в межах дошки
			return True

	# функція для створення дамки
	def king(self, coords):
		"""
		Takes in coords, the coordinates of square to be considered for kinging.
		If it meets the criteria, then king() kings the piece in that square and kings it.
		"""
		x, y = coords
		# якщо поле зайняте шашкою
		if self.location(coords).busy != None:
			# якщо шашка синя і знаходиться у першому ряді
			# або якщо шашка червона і знаходиться у восьмому ряду
			if (self.location(coords).busy.color == BLUE and y == 0) or (self.location(coords).busy.color == RED and y == 7):
				# то ця шашка є дамкою
				self.location(coords).busy.king = True 

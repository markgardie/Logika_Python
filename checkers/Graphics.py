
import pygame
from constants import*

pygame.init()

class Graphics:
	# конструктор
	# налаштування вікна та графічних елементів
	def __init__(self):
		# надпис вікна
		self.caption = "Checkers"

		# кількість кадрів в секунду
		self.fps = 60
		# годинник
		# тікає і вказує, коли треба змінити кадри
		self.clock = pygame.time.Clock()

		# розміри вікна
		self.window_size = 600
		# створення екрану, вікна
		self.screen = pygame.display.set_mode((self.window_size, self.window_size))
		# завантаження фону дошки
		self.background = pygame.image.load('checkers/resources/board.png')

		# розмір поля дорівнює розміру вікна, яке поділене на 8
		# бо у нас дошка 8 на 8
		self.square_size = self.window_size / 8
		# розмір шашки в два рази менше поля
		self.piece_size = self.square_size / 2

		# чи треба виводити повідомлення про перемоги
		self.message = False

	# налаштування вікна
	def setup_window(self):
		"""
		This initializes the window and sets the caption at the top.
		"""
		# запускаємо пайгейм для роботи з текстом
		pygame.init()
		# виставляємо надпис вікна
		pygame.display.set_caption(self.caption)

	# оновлення вікна
	def update_display(self, board, legal_moves, selected_piece):
		"""
		This updates the current display.
		"""
		# малюємо фон
		self.screen.blit(self.background, (0,0))
		
		# підсвічуємо обрану шашку та дозволені ходи
		self.highlight_squares(legal_moves, selected_piece)
		# малюємо шашки
		self.draw_board_pieces(board)

		# якщо треба вивести повідомлення
		if self.message:
			# виводимо повідомлення на екран
			self.screen.blit(self.text_surface_obj, self.text_rect_obj)

		# оновлюємо екран
		pygame.display.update()
		# тіки годинника
		self.clock.tick(self.fps)

	# малювання квадратів
	def draw_board_squares(self, board):
		"""
		Takes a board object and draws all of its squares to the display
		"""
		# 8 рядів, 8 стовпців
		for x in range(8):
			for y in range(8):
				# rect - функція, яка малює квадрати
				# x * self.square_size - це переклад координат дошки в піксенльні координати
				# малюємо на екрані screen
				# з певним кольором
				pygame.draw.rect(self.screen, board[x][y].color, (x * self.square_size, y * self.square_size, self.square_size, self.square_size), )
	
	# малювання шашок
	def draw_board_pieces(self, board):
		"""
		Takes a board object and draws all of its pieces to the display
		"""
		# 8 рядів, 8 стовпців
		for x in range(8):
			for y in range(8):
				# якщо поле зайнято шашкою
				if board.matrix[x][y].busy != None:
					# малюємо шашку, коло, circle
					# на екрані
					# з певним кольором
					pygame.draw.circle(self.screen, board.matrix[x][y].busy.color, (self.pixel_coords((x,y))), self.piece_size) 

					# якщо шашка опинилась дамкою
					if board.location((x,y)).busy.king == True:
						# то додаємо золоту GOLD підсвітку
						pygame.draw.circle(self.screen, GOLD, self.pixel_coords((x,y)), int (self.piece_size / 1.7), int(self.piece_size / 4))

	# переклад координат дошки (8 на 8) в піксельні координати (600 на 600)
	def pixel_coords(self, board_coords):
		"""
		Takes in a tuple of board coordinates (x,y) 
		and returns the pixel coordinates of the center of the square at that location.
		"""
		# для переклад треба помножити координати дошки на розмір полів, квадратів
		return (board_coords[0] * self.square_size + self.piece_size, board_coords[1] * self.square_size + self.piece_size)

	# переклад піксельних координат (600 на 600) в координати дошки (8 на 8)
	def board_coords(self, pixel):
		"""
		Does the reverse of pixel_coords(). Takes in a tuple of of pixel coordinates and returns what square they are in.
		"""
		# тут треба навпаки поділит піксельні координати на розмір поля
		return (int(pixel[0] / self.square_size), int(pixel[1] / self.square_size))	

	# підсвітка полів можливих кроків та шашки, на яку натиснули
	def highlight_squares(self, squares, origin):
		"""
		Squares is a list of board coordinates. 
		highlight_squares highlights them.
		"""
		# проходимось по всім квадратам, полям
		for square in squares:
			# змінюємо колір на HIGH
			pygame.draw.rect(self.screen, HIGH, (square[0] * self.square_size, square[1] * self.square_size, self.square_size, self.square_size))	

		# якщо було натиснуто на якусь шашку
		if origin != None:
			# її також підсвічуємо
			pygame.draw.rect(self.screen, HIGH, (origin[0] * self.square_size, origin[1] * self.square_size, self.square_size, self.square_size))

	# малювання повідомлення про перемогу
	def draw_message(self, message):
		"""
		Draws message to the screen. 
		"""
		# вказуємо, що треба виводити повідомлення
		self.message = True
		# створюємо шрифт з розміром 44, назвою freesansbold
		self.font_obj = pygame.font.Font('freesansbold.ttf', 44)
		# створюємо текст на основі шрифта
		self.text_surface_obj = self.font_obj.render(message, True, HIGH, BLACK)
		#  отримуємо хітбокс, фон тексту
		self.text_rect_obj = self.text_surface_obj.get_rect()
		# розміщуємо хітбокс тексту і відповідно сам текст всередині екрану (ділимо на два розміри екрану)
		self.text_rect_obj.center = (self.window_size / 2, self.window_size / 2)
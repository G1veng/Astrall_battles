import pygame

class EmptySquare():
	def __init__(self, start_position_x, start_position_y, count_squares, ab_game):
		self.image = pygame.image.load("D:\\Python\\Astrall_battles\\Images\\empty_square.bmp")
		self.screen = ab_game
		self.count = count_squares
		self.squares = []
		self.is_empty = []
		for i in range(count_squares):
			self.squares.append(self._create_square(start_position_x + i * (106 + 40), start_position_y))
			self.is_empty.append(True)

	def _create_square(self, x, y):
		rect = self.image.get_rect()
		rect.x = x
		rect.y = y
		return rect

	def blitme(self):
		for i in range(self.count):
			self.screen.blit(self.image, self.squares[i])

	def find_first_empty(self):
		for i in range(len(self.is_empty)):
			if self.is_empty[i] == True:
				self.is_empty[i] = False
				return [self.squares[i], i]

	def is_have_empty(self):
		for i in range(len(self.is_empty)):
			if self.is_empty[i] == True:
				return True
		return False

	def set_all_empty(self):
		for i in range(len(self.is_empty)):
			self.is_empty[i] = True
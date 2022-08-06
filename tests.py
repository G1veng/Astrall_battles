import unittest
import db_data
import empty_square
import pygame

class AstrallBattleTest(unittest.TestCase):
	def test_get_path_db(self):
		answer = db_data.get_path("goblin")
		self.assertEqual(answer, "goblin_image")

	def test_collect_path(self):
		answer = db_data.collect_path("goblin_image")
		self.assertEqual(answer, 'D:\\Python\\Astrall_battles\\Images\\goblin_image.bmp')

	def test_get_description(self):
		answer = db_data.get_description("goblin")
		self.assertEqual(answer, "Some information about this hero")

	def test_empty_square_draw(self):
		answer = empty_square.EmptySquare(0, 0, 2, None)
		image = pygame.image.load("Images/empty_square.bmp")
		rect = image.get_rect()
		rect.x = 0
		rect.y = 0
		rect2 = image.get_rect()
		rect2.x = 146
		rect2.y = 0
		self.assertEqual([rect, rect2], answer.squares)

	def test_get_path_via_index(self):
		answer = db_data.get_path_via_index(1)
		self.assertEqual(answer, "goblin_image")
		

if __name__ == '__main__':
	unittest.main()
import unittest
import db_data
import empty_square
import pygame

class AstrallBattleTest(unittest.TestCase):
	def test_get_path_db(self):
		answer = db_data.get_path("Fire drake")
		self.assertEqual(answer, "firedrake")

	def test_collect_path(self):
		answer = db_data.collect_path("firedrake")
		self.assertEqual(answer, 'D:\\Python\\Astrall_battles\\Images\\Cards\\Fire\\firedrake.bmp')

	def test_get_description(self):
		answer = db_data.get_description("Fire drake")
		self.assertEqual(answer, "Fire Drake attacks the same turn as summoned")

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
		self.assertEqual(answer, "firedrake")
		
	def test_get_card_elem(self):
		answer = db_data.get_cards_of_element("Holy")
		self.assertEqual(answer[5], 1)	

if __name__ == '__main__':
	unittest.main()
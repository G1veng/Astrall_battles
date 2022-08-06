import pygame
import settings as sett

class DrawText():
	def __init__(self, ab_game, card, text):
		self.settings = sett.Settings()
		self.screen = ab_game
		self.msg = text
		self.font = pygame.font.SysFont(None, 20)
		self.bg_color = self.settings.bg_color
		self.text_color = (0, 0, 0)

		self.msg_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.x = card.rect.x + card.image.get_height()
		self.msg_image_rect.y = card.rect.y + card.image.get_width() // 2


	def blitme(self):
		self.screen.blit(self.msg_image, self.msg_image_rect)


class Text():
	def __init__(self, ab_game, text, x, y):
		self.settings = sett.Settings()
		self.screen = ab_game
		self.msg = text
		self.font = pygame.font.SysFont(None, 22)
		self.bg_color = self.settings.bg_color
		self.text_color = (0, 0, 0)

		self.msg_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.x = x
		self.msg_image_rect.y = y

	def blitme(self):
		self.screen.blit(self.msg_image, self.msg_image_rect)

	def set_text(self, text):
		self.msg_image = self.font.render(text, True, self.text_color, self.bg_color)
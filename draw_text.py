from cgitb import text
from socket import inet_ntoa
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

class New_Text():
	set = sett.Settings()
	bg_cl = set.bg_color

	def __init__(self, ab_game, text, x, y, t_color=(255,0,60), bg_color=bg_cl, font_size=22):
		self.settings = sett.Settings()
		self.screen = ab_game
		self.msg = text
		self.font = pygame.font.SysFont(None, font_size)
		self.bg_color = bg_color
		self.text_color = t_color

		self.msg_image = self.font.render(self.msg, True, self.text_color)
		self.msg_image.set_alpha(350)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.x = x
		self.msg_image_rect.y = y

	def blitme(self):
		self.screen.blit(self.msg_image, self.msg_image_rect)

	def set_coordinates(self, x, y):
		self.msg_image_rect.x = x
		self.msg_image_rect.y = y

	def set_text(self, text):
		self.msg_image = self.font.render(text, True, self.text_color, self.bg_color)

	
class Texts():
	set = sett.Settings()
	bg_cl = set.bg_color

	def __init__(self, ab_game, texts, x, y, t_color=(255,0,60), bg_color=bg_cl, font_size=22):
		self.inner_texts = []

		for i in range(len(texts)):
			self.inner_texts.append(New_Text(ab_game, texts[i], x, y + i * 20, t_color=t_color, bg_color=bg_color, font_size=font_size))
		
	def blitme(self):
		for text in self.inner_texts:
			text.blitme()
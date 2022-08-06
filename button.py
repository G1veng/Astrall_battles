import pygame.font

class Button():
	def __init__(self, ab_game, msg, pos_x, pos_y):
		self.screen = ab_game.screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 110, 40
		self.button_color = (0, 0, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 50)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = pos_x
		self.rect.y = pos_y

		self.prep_msg(msg)

	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.rect

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
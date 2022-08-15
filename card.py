from re import S
import pygame
import db_data
import draw_text
import settings

class ActiveCard():
	def __init__(self, ab_game, card):
		self.inner_name = card.inner_name
		self.screen = ab_game
		self.settings = settings.Settings()
		self.healt = db_data.get_healt(card.inner_name)
		self.cost = db_data.get_cost(card.inner_name)
		self.damage = db_data.get_damage(card.inner_name)
		self.image = pygame.image.load(db_data.collect_path(db_data.get_path(card.inner_name)))
		self.image = pygame.transform.scale(self.image, (self.settings.picture_weight, self.settings.picture_height))
		self.element = db_data.get_element(card.inner_name)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.is_active = False
		self.is_first_rount = True
		self.skill = db_data.get_skill_by_name(self.inner_name)
		self.stun = False

		self.cost = int(db_data.get_cost(self.inner_name))
		self.damage = int(db_data.get_damage(self.inner_name))
		self.hp = int(db_data.get_healt(self.inner_name))

		self.cost_text = draw_text.New_Text(self.screen, str(self.cost), self.rect.x, self.rect.y, font_size=30, t_color=(0, 0, 0))
		self.damage_text = draw_text.New_Text(self.screen, str(self.damage),
			self.rect.x + self.image.get_height() - 20, self.rect.y + self.image.get_width() - 20, font_size=30, t_color=(255,0,60))
		self.hp_text = draw_text.New_Text(self.screen, str(self.hp),
			self.rect.x, self.rect.y + self.image.get_width() - 20, font_size=30, t_color=(0, 255, 50))

		#self.healt_text = draw_text.Text(self.screen, "HP: " + str(self.healt), self.rect.x, self.rect.y)
		#self.damage_text = draw_text.Text(self.screen, "DMG: " + str(self.damage), self.rect.x, self.rect.y)

	def blitme(self):
		self.screen.blit(self.image, self.rect)
		"""self.healt_text.msg_image_rect.y = self.rect.y - 20
		self.healt_text.msg_image_rect.x = self.rect.x - 10
		self.damage_text.msg_image_rect.y = self.rect.y - 20
		self.damage_text.msg_image_rect.x = self.rect.x + 50
		self.healt_text = draw_text.Text(self.screen, "HP: " + str(self.healt), self.rect.x, self.rect.y - 20)
		self.healt_text.blitme()
		self.damage_text.blitme()"""
		self.cost_text.set_coordinates(self.rect.x, self.rect.y)
		self.damage_text.set_coordinates(self.rect.x + self.image.get_height() - 20, self.rect.y + self.image.get_width() - 20)
		self.hp_text.set_coordinates(self.rect.x, self.rect.y + self.image.get_width() - 20)
		self.cost_text.blitme()
		self.damage_text.blitme()
		self.hp_text.blitme()

class Head():
	def __init__(self, ab_game, name, position_x, position_y):
		self.is_active = True
		self.inner_name = name
		self.screen = ab_game
		self.screen_rect = ab_game.get_rect()

		self.hp = db_data.get_head_health(name)
		self.image = pygame.image.load(db_data.collect_head_path(db_data.get_head_path(name)))
		self.rect = self.image.get_rect()

		self.rect.x = position_x
		self.rect.y = position_y

	def blitme(self):
		if self.is_active:
			self.screen.blit(self.image, self.rect)

class Card():
	def __init__(self, ab_game, name, position_x, position_y):
		self.is_active = True
		self.inner_name = name
		self.screen = ab_game
		self.screen_rect = ab_game.get_rect()
		self.settings = settings.Settings()

		self.image = pygame.image.load(db_data.collect_path(db_data.get_path(name)))
		self.image = pygame.transform.scale(self.image, (self.settings.picture_weight, self.settings.picture_height))
		self.rect = self.image.get_rect()

		self.cost = int(db_data.get_cost(self.inner_name))
		self.damage = int(db_data.get_damage(self.inner_name))
		self.hp = int(db_data.get_healt(self.inner_name))

		self.cost_text = draw_text.New_Text(self.screen, str(self.cost), position_x, position_y, font_size=30, t_color=(0, 0, 0))
		self.damage_text = draw_text.New_Text(self.screen, str(self.damage),
			position_x + self.image.get_height() - 20, position_y + self.image.get_width() - 20, font_size=30, t_color=(255,0,60))
		self.hp_text = draw_text.New_Text(self.screen, str(self.hp),
			position_x, position_y + self.image.get_width() - 20, font_size=30, t_color=(0, 255, 50))

		self.rect.x = position_x
		self.rect.y = position_y

	def blitme(self):
		if self.is_active:
			self.screen.blit(self.image, self.rect)
			self.cost_text.blitme()
			self.damage_text.blitme()
			self.hp_text.blitme()


class CreateDeck():
	def __init__(self, ab_game, start_index, end_index, start_position_x, start_position_y, element):
		self.cards = []
		for i in range(start_index, end_index + 1):
			real_i = i - start_index
			if i >= len(db_data.get_cards_of_element(element)):
				break
			self.cards.append(Card(ab_game, db_data.get_cards_of_element(element)[i][5], start_position_x + real_i * 146, start_position_y))

	def blitme(self):
		for card in self.cards:
			if card.is_active == True:
				card.blitme()
import enum

class Settings():
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		self.is_description_active = False
		self.count_of_cards_in_hand = 6
		self.part_of_the_game = PartsOfGame.CHOOSE_CARDS_P1
		self.turn = Players.PLAYER_ONE
		self.start_gaming_points = 4
		self.elements_count = 13

		self.picture_weight = 110
		self.picture_height = 110

		self.text_length = 35
		self.mana_increase_player_one = 1
		self.mana_increase_player_two = 1
		self.mana_increase_player_one_test = {"Air":1, "Fire":1, "Earth":1}
		self.mana_increase_player_two_test = {"Air":1, "Fire":1, "Earth":1}


class PartsOfGame(enum.Enum):
	CHOOSE_CARDS_P1 = 1,
	CHOOSE_CARDS_P2 = 2,
	BATTLE = 3,
	ENDING = 4,
	INTERMEDIATE_SCREEN = 5,
	CHOOSE_HEAD_P1 = 6,
	CHOOSE_HEAD_P2 = 7,


class Players(enum.Enum):
	PLAYER_ONE = 1,
	PLAYER_TWO = 2,


class Elements():
	def get_element(self, id):
		if id == 1:
			return "Fire"
		if id == 2:
			return "Water"
		if id == 3:
			return "Air"
		if id == 4:
			return "Earth"
		if id == 5:
			return "Beast"
		if id == 6:
			return "Chaos"
		if id == 7:
			return "Control"
		if id == 8:
			return "Death"
		if id == 9:
			return "Demonic"
		if id == 10:
			return "Holy"
		if id == 11:
			return "Illusion"
		if id == 12:
			return "Mechanical"
		if id == 13:
			return "Sorcery"

	def get_elements_count(self):
		return 13
		
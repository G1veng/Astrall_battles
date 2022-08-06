import enum

class Settings():
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		self.is_description_active = False
		self.count_of_cards_in_hand = 5
		self.part_of_the_game = PartsOfGame.CHOOSE_CARDS_P1
		self.turn = Players.PLAYER_ONE
		self.start_gaming_points = 4


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
	def __init__(self, element):
		if element == 1:
			return "Fire"
		if element == 2:
			return "Water"
		if element == 3:
			return "Air"
		if element == 4:
			return "Earth"
		if element == 5:
			return "Beast"
		if element == 6:
			return "Chaos"
		if element == 7:
			return "Control"
		if element == 8:
			return "Death"
		
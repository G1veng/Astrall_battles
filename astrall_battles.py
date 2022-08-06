import sys
import pygame
import settings as Set
from card import Card
from card import CreateDeck
from card import ActiveCard
from card import Head
import db_data
import draw_text
import empty_square
import button

class AstralBattles():
    def __init__(self):
        pygame.init()
        self.settings = Set.Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #region P1_CHOOSE_DECK
        pygame.display.set_caption("Astrall Battles")
        self.end_index_available_card = 5
        self.start_index_available_card = 1
        self.available_cards = CreateDeck(self.screen, self.start_index_available_card, self.end_index_available_card, 250, 100)
        #self.description = draw_text.DrawText(self.screen, self.card, db_data.get_description(self.card.inner_name))
        self.users_deck = empty_square.EmptySquare(250, 600, self.settings.count_of_cards_in_hand, self.screen)
        self.available_cards_empty_squares = empty_square.EmptySquare(250, 100, self.settings.count_of_cards_in_hand, self.screen)
        self.chosen_cards = []
        self.button_next = button.Button(self, 'Next', 1000, 125)
        self.button_prev = button.Button(self, 'Prev', 100, 125)
        self.button_next_phase = button.Button(self, 'Finish', 1000, 650)
        #endregion
        #region BATTLE
        self.is_first_round = True
        self.player_one = draw_text.Text(self.screen, "Player 1", 20, 20)
        self.player_two = draw_text.Text(self.screen, "Player 2", 20, 20)
        self.player_one_deck = []
        self.player_two_deck = []
        self.player_one_mana = {"Fire": self.settings.start_gaming_points, "Water": self.settings.start_gaming_points,
         "Air": self.settings.start_gaming_points, "Earth": self.settings.start_gaming_points}
        self.player_two_mana = {"Fire": self.settings.start_gaming_points, "Water": self.settings.start_gaming_points,
         "Air": self.settings.start_gaming_points, "Earth": self.settings.start_gaming_points}
        self.player_one_head = None
        self.player_two_head = None
        self.mana = []
        self.field = []
        self.player_one_space = empty_square.EmptySquare(350, 250, self.settings.count_of_cards_in_hand, self.screen)
        self.player_two_space = empty_square.EmptySquare(350, 100, self.settings.count_of_cards_in_hand, self.screen)
        self.player_one_played_cards = [None, None, None, None, None]
        self.player_two_played_cards = [None, None, None, None, None]
        self.button_next_turn = button.Button(self, "Finish", 1000, 600)
        self.button_pressed = True
        self.player_one_head = None
        self.player_two_head = None
        self.player_one_health = None
        self.player_two_health = None
        #region Intermidiate
        self.prev_player = Set.Players.PLAYER_ONE
        self.next_player_button = button.Button(self, "Next", self.screen.get_width() // 2, self.screen.get_height() // 2)
        #endregion Intermidiate
        #region ChooseHeadPart
        self.head_x = 300
        self.head_y = 50
        self.head_gap = 150
        self.heads = [empty_square.EmptySquare(self.head_x, self.head_y, 5, self.screen),
            empty_square.EmptySquare(self.head_x, self.head_y + 1 * self.head_gap, 5, self.screen), 
            empty_square.EmptySquare(self.head_x, self.head_y + 2 * self.head_gap, 5, self.screen),
            empty_square.EmptySquare(self.head_x, self.head_y + 3 * self.head_gap, 5, self.screen), 
            empty_square.EmptySquare(self.head_x, self.head_y + 4 * self.head_gap, 5, self.screen), ]
        self.heads_pictures = []
        self.curren_min = 0
        self.button_next_heads = button.Button(self, "Next", self.screen.get_width() - 120, self.screen.get_height() // 2 + 100)
        self.button_prev_heads = button.Button(self, "Prev", self.screen.get_width() - 120, self.screen.get_height() // 2 - 100)
        self.button_finish_chose_head = button.Button(self, "Finish", self.screen.get_width() - 120, self.screen.get_height() // 2 + 200)
        counter = self.curren_min
        for i in range(0, len(self.heads)):
            for j in range(0, len(self.heads)):
                counter += 1
                if counter <= db_data.get_count_of_heads():
                    self.heads_pictures.append(Head(self.screen, counter, self.heads[i].squares[j][0], self.heads[i].squares[j][1]))
        #endregion ChooseHeadPart
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    if event.key == pygame.K_RIGHT:
                        if self.settings.part_of_the_game == Set.PartsOfGame.INTERMEDIATE_SCREEN:
                            self.change_intermediate_screen()
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_CARDS_P1:
                        self._choose_cards_part()
                    if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_CARDS_P2:
                        self._choose_cards_part()    
                    if self.settings.part_of_the_game == Set.PartsOfGame.BATTLE:
                        self._battle_part()
                    if self.settings.part_of_the_game == Set.PartsOfGame.INTERMEDIATE_SCREEN:
                        self.intermidiate_screen()
                    if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P1 or self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P2:
                        self.choose_head_part()

            self.screen.fill(self.settings.bg_color)
            if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_CARDS_P1:
                self._draw_field_choose_cards_part()
            if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_CARDS_P2:
                self._draw_field_choose_cards_part()
            if self.settings.part_of_the_game == Set.PartsOfGame.BATTLE:
                self._draw_battle_part()
            if self.settings.part_of_the_game == Set.PartsOfGame.ENDING:
                self.ending()
            if self.settings.part_of_the_game == Set.PartsOfGame.INTERMEDIATE_SCREEN:
                self.draw_intermidiate_screen()
            if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P1 or self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P2:
                self.draw_choose_head_part()
            pygame.display.flip()


    def choose_head_part(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_next_heads.rect.collidepoint(mouse_pos):
            if self.curren_min + 25 <= db_data.get_count_of_heads():
                self.curren_min += 5
                self._slide_heads_up()
                for i in range(self.settings.count_of_cards_in_hand):
                    self.heads_pictures[4 * self.settings.count_of_cards_in_hand + i] = Head(self.screen,
                        self.curren_min + 4 * self.settings.count_of_cards_in_hand + i, 
                        self.heads[4].squares[i][0],
                        self.heads[4].squares[i][1])
        if self.button_prev_heads.rect.collidepoint(mouse_pos):
            if self.curren_min >= 5:
                self.curren_min -= 5
                self._slide_heads_down()
                for i in range(self.settings.count_of_cards_in_hand):
                    self.heads_pictures[i] = Head(self.screen,
                        self.curren_min + i + 1, 
                        self.heads[0].squares[i][0],
                        self.heads[0].squares[i][1])
        for head in self.heads_pictures:
            if head:
                if head.rect.collidepoint(mouse_pos):
                    if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P1:
                        self.player_one_head = Head(self.screen,
                            head.inner_name, self.screen.get_width() // 10,
                            self.screen.get_height() // 2 - 50)
                    if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P2:
                        self.player_two_head = Head(self.screen,
                            head.inner_name, self.screen.get_width() // 10,
                            self.screen.get_height() // 2 - 50)
        if self.button_finish_chose_head.rect.collidepoint(mouse_pos):
            if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P1:
                if self.player_one_head:
                    self.settings.part_of_the_game = Set.PartsOfGame.CHOOSE_HEAD_P2
            if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P2:
                if self.player_two_head:
                    self.player_one_health = draw_text.Text(self.screen, "HP: " + str(self.player_one_head.hp), 150, 400)
                    self.player_two_health = draw_text.Text(self.screen, "HP: " + str(self.player_two_head.hp), 150, 30)
                    self.settings.part_of_the_game =Set.PartsOfGame.BATTLE


    def draw_choose_head_part(self):
        self.button_next_heads.draw_button()
        self.button_prev_heads.draw_button()
        self.button_finish_chose_head.draw_button()
        for head in self.heads:
            if head:
                head.blitme()
        for head_picture in self.heads_pictures:
            if head_picture:
                head_picture.blitme()
        if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P1:
            if self.player_one_head:
                self.player_one_head.blitme()
        if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_HEAD_P2:
            if self.player_two_head:
                self.player_two_head.blitme()
        

    def _slide_heads_up(self):
        for i in range(1, len(self.heads)):
            for j in range(0, len(self.heads)):
                self.heads_pictures[i * 5 + j].rect.x = self.heads[i - 1].squares[j][0]
                self.heads_pictures[i * 5 + j].rect.y = self.heads[i - 1].squares[j][1]
                self.heads_pictures[(i - 1) * 5 + j] = self.heads_pictures[i * 5 + j]
        for i in range(len(self.heads)):
            self.heads_pictures[4 * 5 + i] = None


    def _slide_heads_down(self):
        for i in range(3, -1, -1):
            for j in range(0, len(self.heads)):
                self.heads_pictures[i * 5 + j].rect.x = self.heads[i + 1].squares[j][0]
                self.heads_pictures[i * 5 + j].rect.y = self.heads[i + 1].squares[j][1]
                self.heads_pictures[(i + 1) * 5 + j] = self.heads_pictures[i * 5 + j]
        for i in range(len(self.heads)):
            self.heads_pictures[i] = None


    def draw_intermidiate_screen(self):
        self.next_player_button.draw_button()


    def intermidiate_screen(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.next_player_button.rect.collidepoint(mouse_pos):
            self.change_intermediate_screen()


    def ending(self):
        if self.player_one_head.hp <= 0:
            self.who_won = draw_text.Text(self.screen, "Player 2 wins", self.screen.get_width() // 2, self.screen.get_height() // 2)
        if self.player_two_head.hp <= 0:
            self.who_won = draw_text.Text(self.screen, "Player 1 wins", self.screen.get_width() // 2, self.screen.get_height() // 2)
        self.who_won.blitme()


    def change_intermediate_screen(self):
        if self.settings.part_of_the_game == Set.PartsOfGame.INTERMEDIATE_SCREEN:
            self.settings.part_of_the_game = Set.PartsOfGame.BATTLE


    def _battle_part(self):
        mouse_pos = pygame.mouse.get_pos()
        self.button_pressed = False
        #First player
        if self.settings.turn == Set.Players.PLAYER_ONE:
            for card in self.player_one_deck:
                if card.rect.collidepoint(mouse_pos):
                    for inner_card in self.player_one_deck:
                        inner_card.is_active = False
                    if self.player_one_mana[card.element] >= card.cost:
                        card.is_active = True
            for i in range(len(self.player_one_space.squares)):
                if self.player_one_space.squares[i].collidepoint(mouse_pos) and self.player_one_space.is_empty[i]:
                    for card in self.player_one_deck:
                        if card.is_active:
                            self.player_one_space.is_empty[i] = False
                            new_card = ActiveCard(self.screen, card)
                            new_card.rect.x = self.player_one_space.squares[i].x
                            new_card.rect.y = self.player_one_space.squares[i].y
                            self.player_one_played_cards[i] = new_card
                            self.player_one_mana[card.element] -= card.cost
                            for inner_card in self.player_one_deck:
                                inner_card.is_active = False
            if self.button_next_turn.rect.collidepoint(mouse_pos) and not self.button_pressed:
                self.button_pressed = True
                for value in self.player_one_mana:
                    self.player_one_mana[value] += 1
                if not self.is_first_round:
                    self._player_one_cards_atack()
                self.settings.turn = Set.Players.PLAYER_TWO
                self.settings.part_of_the_game = Set.PartsOfGame.INTERMEDIATE_SCREEN
        #Second Player
        if self.settings.turn == Set.Players.PLAYER_TWO:
            for card in self.player_two_deck:
                if card.rect.collidepoint(mouse_pos):
                    for inner_card in self.player_two_deck:
                        inner_card.is_active = False
                    if self.player_two_mana[card.element] >= card.cost:
                        card.is_active = True
            for i in range(len(self.player_two_space.squares)):
                if self.player_two_space.squares[i].collidepoint(mouse_pos) and self.player_two_space.is_empty[i]:
                    for card in self.player_two_deck:
                        if card.is_active:
                            self.player_two_space.is_empty[i] = False
                            new_card = ActiveCard(self.screen, card)
                            new_card.rect.x = self.player_two_space.squares[i].x
                            new_card.rect.y = self.player_two_space.squares[i].y
                            self.player_two_played_cards[i] = new_card
                            self.player_two_mana[card.element] -= card.cost
                            for inner_card in self.player_two_deck:
                                inner_card.is_active = False
            if self.button_next_turn.rect.collidepoint(mouse_pos) and not self.button_pressed:
                self.button_pressed = True
                for value in self.player_two_mana:
                    self.player_two_mana[value] += 1
                if not self.is_first_round:
                    self._player_two_cards_atack()
                if self.is_first_round:
                    self.is_first_round = False
                self.settings.turn = Set.Players.PLAYER_ONE
                self.settings.part_of_the_game = Set.PartsOfGame.INTERMEDIATE_SCREEN


    def _player_one_cards_atack(self):
        for i in range(len(self.player_one_played_cards)):
            if self.player_one_played_cards[i]:
                if self.player_two_played_cards[i]:
                    self.player_two_played_cards[i].healt -= self.player_one_played_cards[i].damage
                    if self.player_two_played_cards[i].healt <= 0:
                        self.player_two_played_cards[i] = None
                        self.player_two_space.is_empty[i] = True
                else:
                    self.player_two_head.hp -= self.player_one_played_cards[i].damage
                    if self.player_two_head.hp <= 0:
                        self.settings.part_of_the_game = Set.PartsOfGame.ENDING


    def _player_two_cards_atack(self):
        for i in range(len(self.player_two_played_cards)):
            if self.player_two_played_cards[i]:
                if self.player_one_played_cards[i]:
                    self.player_one_played_cards[i].healt -= self.player_two_played_cards[i].damage
                    if self.player_one_played_cards[i].healt <= 0:
                        self.player_one_played_cards[i] = None
                        self.player_one_space.is_empty[i] = True
                else:
                    self.player_one_head.hp -= self.player_two_played_cards[i].damage
                    if self.player_one_head.hp <= 0:
                        self.settings.part_of_the_game = Set.PartsOfGame.ENDING


    def _draw_battle_part(self):
        self.player_one_space.blitme()
        self.player_two_space.blitme()
        self.player_one_head.blitme()
        self.player_two_head.blitme()
        if self.settings.turn == Set.Players.PLAYER_ONE:
            self._flip_to_player_one()
            for card in self.player_one_deck:
                card.blitme()
            self.player_one.blitme()
        for card in self.player_one_played_cards:
            if card:
                card.blitme()    
        if self.settings.turn == Set.Players.PLAYER_TWO:  
            self._flip_to_player_two()   
            for card in self.player_two_deck:
                card.blitme()
            self.player_two.blitme()
        for card in self.player_two_played_cards:
            if card:
                card.blitme()
        self._draw_mana()
        self.button_next_turn.draw_button()
        self.player_one_health.set_text("HP: " + str(self.player_one_head.hp))
        self.player_two_health.set_text("HP: " + str(self.player_two_head.hp))
        self.player_one_health.blitme()
        self.player_two_health.blitme()


    def _flip_to_player_one(self):
        player_one_healt = draw_text.Text(self.screen, str(self.player_one_head.hp), 50, 260)
        self.player_one_head.rect.y = 250
        self.player_two_head.rect.y = 50
        if self.player_one_space.squares[0].y < self.player_two_space.squares[0].y:
            for space in self.player_one_space.squares:
                space.y += 150
            for card in self.player_one_played_cards:
                if card:
                    card.rect.y += 150
            for space in self.player_two_space.squares:
                space.y -= 150
            for card in self.player_two_played_cards:
                if card:
                    card.rect.y -= 150
            self.player_one_health.msg_image_rect.y = 400
            self.player_two_health.msg_image_rect.y = 30


    def _flip_to_player_two(self):
        self.player_one_head.rect.y = 50
        self.player_two_head.rect.y = 250    
        if self.player_two_space.squares[0].y < self.player_one_space.squares[0].y:
            for space in self.player_two_space.squares:
                space.y += 150
            for card in self.player_two_played_cards:
                if card:
                    card.rect.y += 150
            for space in self.player_one_space.squares:
                space.y -= 150
            for card in self.player_one_played_cards:
                if card:
                    card.rect.y -= 150
            self.player_two_health.msg_image_rect.y = 400
            self.player_one_health.msg_image_rect.y = 30


    def isInt(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False


    def _draw_mana(self):
        self.mana = []
        if self.settings.turn == Set.Players.PLAYER_ONE:
            for i in range(len(self.player_one_mana)):
                self.mana.append(draw_text.Text(self.screen, self.get_element(i), 50, 450 + i * 30))
                self.mana[i].blitme()
        self.mana = []
        if self.settings.turn == Set.Players.PLAYER_TWO:
            for i in range(len(self.player_two_mana)):
                self.mana.append(draw_text.Text(self.screen, self.get_element(i), 50, 450 + i * 30))
                self.mana[i].blitme()


    def get_element(self, element):
        part = ""
        if element == 0:
            part = "Fire"
        if element == 1:
            part = "Water"
        if element == 2:
            part = "Air"
        if element == 3:
            part = "Earth"
        if self.settings.turn == Set.Players.PLAYER_ONE:
            number = self.player_one_mana[part]
            return part + " " + str(number)
        if self.settings.turn == Set.Players.PLAYER_TWO:
            number = self.player_two_mana[part]
            return part + " " + str(number)


    def _choose_cards_part(self):
        self._click_on_card()
        self._click_on_button()


    def _draw_field_choose_cards_part(self):
        self.available_cards_empty_squares.blitme()
        self.users_deck.blitme()
        if self.settings.is_description_active:
            self.description.blitme()
        self.available_cards.blitme()
        for chosen_card in self.chosen_cards:
            chosen_card.blitme()
        self.button_next.draw_button()
        self.button_prev.draw_button()
        self.button_next_phase.draw_button()  


    def _click_on_card(self):
        mouse_pos = pygame.mouse.get_pos()
        for card in self.available_cards.cards:
            if card.rect.collidepoint(mouse_pos):
                if self.users_deck.is_have_empty():
                    self._transfer_card_user_deck(card)
                break
        for i in range(len(self.chosen_cards)):
            if self.chosen_cards[i].rect.collidepoint(mouse_pos):
                self.users_deck.is_empty[i] = True
                self.chosen_cards[i].is_active = False
                break


    def _transfer_card_user_deck(self, card):
        empty = self.users_deck.find_first_empty()
        if(len(self.chosen_cards) <= empty[1]):
            self.chosen_cards.append(Card(self.screen, card.inner_name, empty[0].x, empty[0].y))
        else:    
            self.chosen_cards[empty[1]] = Card(self.screen, card.inner_name, empty[0].x, empty[0].y)


    def _click_on_button(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_next.rect.collidepoint(mouse_pos):
            if not (self.end_index_available_card + 1) > db_data.get_count_row():
                self.end_index_available_card += 1
                self.start_index_available_card += 1
        if self.button_prev.rect.collidepoint(mouse_pos):
            if not self.end_index_available_card == self.settings.count_of_cards_in_hand:
                self.end_index_available_card -= 1
                self.start_index_available_card -= 1
        self.available_cards = CreateDeck(self.screen, self.start_index_available_card, self.end_index_available_card, 250, 100)
        if self.button_next_phase.rect.collidepoint(mouse_pos):
            if self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_CARDS_P1 and self.chosen_cards != []:
                self.settings.part_of_the_game = Set.PartsOfGame.CHOOSE_CARDS_P2
                self._set_deck_for_player_one()
                self.chosen_cards = []
                self.users_deck.set_all_empty()
            elif self.settings.part_of_the_game == Set.PartsOfGame.CHOOSE_CARDS_P2 and self.chosen_cards != []:
                #self.settings.part_of_the_game = Set.PartsOfGame.BATTLE
                self.settings.part_of_the_game = Set.PartsOfGame.CHOOSE_HEAD_P1
                self._set_deck_for_player_two()


    def _set_deck_for_player_one(self):
        for card in self.chosen_cards:
            self.player_one_deck.append(ActiveCard(self.screen, card))
        for i in range(len(self.player_one_deck)):
            self.player_one_deck[i].rect.x = 300 + 146 * i
            self.player_one_deck[i].rect.y = 600


    def _set_deck_for_player_two(self):
        for card in self.chosen_cards:
            self.player_two_deck.append(ActiveCard(self.screen, card))
        for i in range(len(self.player_two_deck)):
            self.player_two_deck[i].rect.x = 300 + 146 * i
            self.player_two_deck[i].rect.y = 600


if __name__ == '__main__':
    ab = AstralBattles()
    ab.run_game()
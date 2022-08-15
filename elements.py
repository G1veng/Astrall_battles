import pygame
import settings
import draw_text

class Elements():
    def __init__(self, ab_game, pos_x, pos_y, fith_element = None):
        self.path = "D:\\Python\\Astrall_battles\\Images\\Elements\\"
        self.type = ".bmp"
        self.settings = settings.Settings()
        self.class_elements = settings.Elements()
        self.gap = 40

        self.elements_image = []
        self.elements_rect = []
        self.elements_text =[]

        self.screen = ab_game.screen
        self.elements = []
        for element_id in range(1, self.class_elements.get_elements_count() + 1):
            element = self.class_elements.get_element(element_id)
            text = draw_text.New_Text(self.screen, str(element), pos_x - 100, 10 + pos_y + element_id * self.gap,
                (0, 0, 0), font_size=25)
            image = pygame.image.load(self.path + str(element) + self.type)
            image = pygame.transform.scale(image, (self.settings.picture_weight // 3, self.settings.picture_height // 3))
            rect = image.get_rect()
            rect.x = pos_x
            rect.y = pos_y + element_id * self.gap
            self.elements_image.append(image)
            self.elements_rect.append(rect)
            self.elements_text.append(text)

    def blitme(self):
        for element in range(len(self.elements_image)):
            self.screen.blit(self.elements_image[element], self.elements_rect[element])
            self.elements_text[element].blitme()
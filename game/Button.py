import pygame
import random
CORNERSTINE = 'data/cornerstone.ttf'

RED = (200, 30, 30)
GREEN = (20, 200, 20)
class Button():
    def __init__(self, x, y, button_text, font_style = CORNERSTINE, font_color = RED, font_size = 20, button_color = GREEN):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.button_text = button_text
        self.font_style = font_style
        self.font_color = font_color
        self.button_color = button_color
        self.button_color2 = list(map(lambda x: x/2, button_color))
        self.active = True
        self.width = len(self.button_text) * self.font_size * 0.6 + 4
        self.height = self.font_size + 2
        self.pressed = False
        #self.font_color_pressed = list(map(lambda x:(x + 70 if x <= 185 else 255), font_color))
        self.button_color_pressed = list(map(lambda x:(x + 70 if x <= 185 else 255), button_color))

        pygame.font.init()

        self.font = pygame.font.Font(font_style, font_size)

    def render(self, screen):
        pygame.draw.rect(screen, self.button_color2, (self.x - 7, self.y - 6, self.width + 10, self.height + 10))
        if self.pressed == False:
            pygame.draw.rect(screen, self.button_color, (self.x - 2, self.y - 1, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.button_color_pressed, (self.x - 2, self.y - 1, self.width, self.height))
        screen.blit(self.font.render(self.button_text, 0, self.font_color), (self.x, self.y))


    def click_check(self, click_x , click_y):
        if click_x >= self.x and click_y <= self.y + self.height and click_y >= self.y and click_x <= self.x + self.width and self.active == True:
            self.pressed = True

    def unpress(self):
        self.pressed = False
        self.use()

    def use(self):
        print('ЭЩКЕРЕ')



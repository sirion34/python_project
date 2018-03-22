import pygame
import random
from Constants import *
from Projective import *
from Mob import *
from Character import *
from Button import *


class Button_Add_Demon(Button):
    def __init__(self, x, y, button_text, game):
        Button.__init__(self, x, y, button_text)
        self.game = game

    def use(self):
        self.game.add_demon(random.randint(0,SCREEN_WIDTH-64), random.randint(0,SCREEN_HEIGHT-64))
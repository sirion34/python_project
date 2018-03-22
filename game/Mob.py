import pygame
import random
from Constants import *
from Projective import *
from Character import *

class  Mob(Character):
    def __init__(self, game, name, x_start, y_start, dir, image_pack, speed):
        Character.__init__(self, game, name, x_start, y_start, dir, image_pack, speed)


class Demon(Mob):
    def __init__(self, game, x_start, y_start, dir):
        self.image_pack = ['data/demonr.png', 'data/demond.png', 'data/demonl.png', 'data/demonu.png']
        Mob.__init__(self, game, 'Demon', x_start, y_start, UP, self.image_pack, 5 )


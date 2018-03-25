import pygame
import random
from Constants import *
from Projective import *

class Skill():

    def __init__(self, name, cd, cost, icon, owner):
        self.name = name
        self.cd = 0
        self.max_cd = cd
        self.cost = cost
        self.icon = pygame.image.load(icon)
        self.owner = owner

        self.font = pygame.font.Font('data/cornerstone.ttf', 70)
        pygame.font.init()

    def click_check(self):
        if self.cd == 0 and self.owner.mp >= self.cost:
            self.owner.mp -= self.cost
            self.cd = self.max_cd
            self.owner.state = SHOOT
            self.owner.spell_casted = pygame.time.get_ticks()

    def use(self):
        pass


    def render(self, screen):
        screen.blit(self.icon, (SCREEN_WIDTH + 2, 300))
        if self.cd > 0:
            tmp = str(self.cd)
            if self.cd > 9999:
                tmp = tmp[0]
            elif self.cd < 1000:
                tmp = '0.' + tmp[0]
            else:
                tmp = tmp[0]

            screen.blit(self.font.render(tmp, 0, BLUE),(SCREEN_WIDTH + 25, 310))


class Aimed_shot(Skill):
    def __init__(self, owner):
        Skill.__init__(self, 'Aimed_shot', 10000, 20, "data/range_aa.png", owner)

    def use(self):
        self.owner.__shoot__()

# class Death_shot(Skill):
#     def __init__(self, owner):
#         Skill.__init__(self, Death_shot, 20000, 20, 'data/')
import pygame
from Constants import *
from Projective import *
from Character import *
from Skills import *

class Player(Character):

    def __init__(self, game, name):
        Character.__init__(self, game, name, START_X, START_Y, RIGHT, PLAYER_IMAGE_PACK, PLAYER_SPEED)
        self.skill_list.append(Aimed_shot(self))

    def render_ui(self,screen):
        #для таблички с ХП и МП (for the plate with HP and MP)
        screen.blit(pygame.image.load('data/hpframe.png'), (self.x + 12, self.y + 58))
        screen.blit(pygame.image.load('data/mpframe.png'), (self.x + 12, self.y + 63))
        m = 1
        z = self.hp // 5
        while m <= z:
            screen.blit(pygame.image.load('data/hptick.png'), (self.x + 11 + m * 2, self.y + 59))
            m += 1
        m = 1
        z = self.mp // 5
        while m <= z:
            screen.blit(pygame.image.load('data/mptick.png'), (self.x + 11 + m * 2, self.y + 64))
            m += 1

        # будущие очки для силы
        # m = 1
        # z = self.sp // 5
        # while m <= z:
        #     screen.blit(pygame.image.load('data/mptick.png'), (self.x + 11 + m * 2, self.y + 64))
        #     m += 1

        [i.render(self.game.screen) for i in self.skill_list]



    def tick(self):
        if self.state != DEAD:
            self.mp += MP_REG
            self.hp += HP_REG
            if self.mp >= MAX_MP:
                self.mp = MAX_MP
            if self.hp >= MAX_HP:
                self.hp = MAX_HP
            if pygame.time.get_ticks() > self.spell_casted + 1000:
                self.state = ALIVE
            if self.hp <= 0:
                self.die()
            for i in self.skill_list:
                if i.cd > 0:
                    i.cd -= pygame.time.get_ticks() - self.previous_tick
                if i.cd < 0:
                    i.cd = 0
                    
            self.previous_tick = pygame.time.get_ticks()


    def shoot_z(self):

        if self.mp >= SKILL1_COST and self.state != SHOOT:

            self.mp -= SKILL1_COST
            self.state = SHOOT
            self.spell_casted = pygame.time.get_ticks()



    def __shoot__(self):
        if self.direction == RIGHT:
            sx = self.x + 12
            sy = self.y
        elif self.direction == DOWN:
            sx = self.x
            sy = self.y + 12
        elif self.direction == LEFT:
            sx = self.x - 12
            sy = self.y
        else:
            sx = self.x
            sy = self.y - 12
        self.game.projective.append(Arrow(self.game, sx, sy, self.direction))

    def __str__(self):

        return (name, self.x, self.y)

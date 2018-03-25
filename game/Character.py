import pygame
import random
from Constants import *
from Projective import *

class Character():

    def __init__(self, game, name, x_start, y_start, dir, image_pack, speed):
        self.game = game
        self.state = ALIVE
        self.direction = dir
        self.x = x_start
        self.y = y_start
        self.size = 48
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.sp = MAX_SP
        self.speed = speed
        self.blocked = [0, 0, 0, 0]
        self.mooving = [0, 0, 0, 0]
        #то, откуда берутся правое, нижнее, левое и верхнее изображение персонажа
        #(then, where do the right, bottom, left and top image of the character)
        self.image_pack = image_pack
        self.images = []
        self.skill_list = []
        self.spell_casted = 0
        self.previous_tick = 0
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []

            #разбиение персонажа
            #первые две начало откуда будет вырезаться на картинке ГГ, вторые две цифры до скольки вырезаться

            ##22.03.2018: почему это ГГ????

            i.append(temp.subsurface(0, 0, 64, 64))
            #изображение для ГГ с натянутой тетивой(image for a GG with a stretched string)
            i.append(temp.subsurface(64, 0, 64, 64))
            #изображение для мертвого ГГ(image for dead gg)
            i.append(temp.subsurface(128, 0, 64, 64))
            self.images.append(i)

    def render(self,screen):
        screen.blit(self.images[self.direction][self.state], (self.x,self.y))

    #что-то связанное с передвижением
    def moove(self):
        self.block_check()
        if self.mooving[RIGHT] == 1 and self.blocked[RIGHT] == 0:
            self.direction = RIGHT
            self.x += self.speed
        if self.mooving[DOWN] == 1 and self.blocked[DOWN] == 0:
            self.direction = DOWN
            self.y += self.speed
        if self.mooving[LEFT] == 1 and self.blocked[LEFT] == 0:
            self.direction = LEFT
            self.x -= self.speed
        if self.mooving[UP] == 1 and self.blocked[UP] == 0:
            self.direction = UP
            self.y -= self.speed



    def block_check(self):
        self.blocked = [0, 0, 0, 0]

        for i in self.game.mobs:
            if self.x != i.x and self.y != i.y:
                self.contact_check(i)
        if self in self.game.mobs:
            self.contact_check(self.game.player)

        if self.x <= 0:
            self.blocked[LEFT] = 1
        if self.y <= 0:
            self.blocked[UP] = 1
        if self.x >= SCREEN_WIDTH - 60:
            self.blocked[RIGHT] = 1
        if self.y >= SCREEN_HEIGHT - 64:
            self.blocked[DOWN] = 1

    def contact_check(self,obj):
        if self.x >= obj.x - obj.size and self.y <= obj.y + obj.size-SIZE_DIF and self.y >= obj.y - obj.size+SIZE_DIF and self.x <= obj.x + SIZE_DIF and obj.state != DEAD:
            self.blocked[RIGHT] = 1
        if self.x <= obj.x + obj.size + SIZE_DIF and self.y <= obj.y + obj.size-SIZE_DIF and self.y >= obj.y - obj.size+SIZE_DIF and self.x >= obj.x + obj.size - SIZE_DIF and obj.state != DEAD:
            self.blocked[LEFT] = 1
        if self.y >= obj.y - self.size and self.x <= obj.x + obj.size-SIZE_DIF and self.x >= obj.x - obj.size+SIZE_DIF and self.y <= obj.y + SIZE_DIF and obj.state != DEAD:
            self.blocked[DOWN] = 1
        if self.y <= obj.y + obj.size + SIZE_DIF and self.x <= obj.x + obj.size-SIZE_DIF and self.x >= obj.x - obj.size+SIZE_DIF and self.y >= obj.y + obj.size - SIZE_DIF and obj.state != DEAD:
            self.blocked[UP] = 1

    #случайное передвижение
    def random_moove(self):
        if self.blocked != [0, 0, 0, 0]:
            self.change_moove(random.randint(0, 3))

    #модуль смены движения в случае столкновения
    def change_moove(self, direction):
        if self.state != DEAD:
            self.mooving = [0, 0, 0, 0]
            self.direction = direction
            if 0 <= direction <= 3:
                self.mooving[direction] = 1

    def stop(self):
        self.mooving = [0, 0, 0, 0]

    def kill(self):
        self.hp = 0
        self.mp = 0
        self.state = DEAD
        self.game.corpses.append(self)
        if self in self.game.mobs:
            self.game.mobs.remove(self)
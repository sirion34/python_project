import pygame
from Constants import *
from Projective import *
class Mob():

    def __init__(self, game, name, x_start, y_start, dir, image_pack):
        self.game = game

        self.state = ALIVE
        self.direction = dir
        self.direction = LEFT
        self.x = x_start
        self.y = y_start
        self.size = 48
        self.size = (64, 64)
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        #то, откуда берутся правое, нижнее, левое и верхнее изображение персонажа
        #(then, where do the right, bottom, left and top image of the character)
        self.image_pack = image_pack
        self.images = []
        self.spell_casted = 0
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []

            #разбиение персонажа
            #первые две начало откуда будет вырезаться на картинке ГГ, вторые две цифры до скольки вырезаться
            # character splitting
            # the first two beginnings from where it will be cut out in the picture of YY,
            # the second two digits before how many are cut out

            i.append(temp.subsurface(0, 0, 64, 64))
            #изображение для ГГ с натянутой тетивой(image for a GG with a stretched string)
            i.append(temp.subsurface(64, 0, 64, 64))
            #изображение для мертвого ГГ(image for dead gg)
            i.append(temp.subsurface(128, 0, 64, 64))
            self.images.append(i)

    def render(self,screen):
        screen.blit(self.images[self.direction][self.state], (self.x,self.y))

class Demon(Mob):
    def __init__(self, game, x_start, y_start, dir):
        self.image_pack = ['data/demonr.png', 'data/demond.png', 'data/demonl.png', 'data/demonu.png']
        self.speed = 10
        Mob.__init__(self, game, 'Demon', x_start, y_start, LEFT, self.image_pack)


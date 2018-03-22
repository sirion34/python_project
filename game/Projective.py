import pygame
from Constants import *

#класс прожектив это родительский класс для всех снарядов
class Projective():
    def __init__(self, game, x_start, y_start, dir, image_pack):
        self.game = game
        self.x = x_start
        self.y = y_start
        self.direction = dir
        #загрузка картинки
        self.image = pygame.image.load(image_pack).convert_alpha()
        self.images = []
        self.images.append(self.image.subsurface(0, 0, 64, 64))
        self.images.append(self.image.subsurface(64, 0, 64, 64))
        self.images.append(self.image.subsurface(128, 0, 64, 64))
        self.images.append(self.image.subsurface(192, 0, 64, 64))

    def render(self, screen):
        screen.blit(self.images[self.direction], (self.x, self.y))

    def moove(self):
        if self.direction == RIGHT:
            self.x += self.speed
        elif self.direction == DOWN:
            self.y += self.speed
        elif self.direction == LEFT:
            self.x -= self.speed
        else:
            self.y -= self.speed
        #проверка выхода за границы экрана

        #проверка на столкновение с мобом и координат наконечника
        self.arrowhead_coords()
        for i in self.game.mobs:
            self.hit_check(i)

        #удаление стрелы в случае вылета за границы
        if self.x > SCREEN_WIDTH or self.x < -32 or self.y > SCREEN_HEIGHT or self.y < -32:
            self.game.projective.remove(self)
    #метод проверки столкновения с мобом
    def hit_check(self, obj):
        if self.arrowhead_x >= obj.x and self.arrowhead_y <= obj.y + obj.size + SIZE_DIF and self.arrowhead_y >= obj.y and self.arrowhead_x <= obj.x +obj.size + SIZE_DIF and obj.state != DEAD:
            obj.kill()
            self.remove()

    #метод нахождения координат наконечника
    def arrowhead_coords(self):
        if self.direction == RIGHT:
            self.arrowhead_x = self.x + 44
            self.arrowhead_y = self.y + 32
        elif self.direction == DOWN:
            self.arrowhead_x = self.x + 32
            self.arrowhead_y = self.y + 44
        elif self.direction == LEFT:
            self.arrowhead_x = self.x + 20
            self.arrowhead_y = self.y + 32
        elif self.direction == UP:
            self.arrowhead_x = self.x + 32
            self.arrowhead_y = self.y + 15

    def remove(self):
        self.game.projective.remove(self)

    def __str__(self):
        return (self.x, self.y)


class Arrow(Projective):
    def __init__(self, game, x_start, y_start, dir):
        # self.x = x_start
        # self.y = y_start
        self.image = 'data/arrow.png'
        self.speed = 10
        Projective.__init__(self, game, x_start, y_start, dir, self.image)

    def __str__(self):
        Projective.__str__()

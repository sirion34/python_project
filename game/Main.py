import pygame
import random
from Constants import *
from Player import *
from pygame.locals import *
from Projective import *
from Mob import *
from Character import *
from Buttons import *

class Main():

    def __init__(self, screen):
        self.screen = screen
        self.camera = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Player(self, 'SIRION')
        self.projective = []
        self.mobs = []
        self.corpses = []
        self.buttons = []
        self.background = pygame.image.load('data/background.jpg')
        self.timer = pygame.time.Clock()
        self.running = True
        self.buttons = []

        self.buttons.append(Button_Add_Demon(SCREEN_HEIGHT + 200, 75, 'ДЬЯВАЛ АДДДД', self))
        self.main_loop()



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
                pygame.quit()
            #эвент регена (regen event)
            elif event.type == USEREVENT + 1:
                self.player.tick()
            #эвент рандомного передвижения
            elif event.type == USEREVENT + 2:
                for i in self.mobs:
                    i.random_moove()
            #передвижение игрока (player movement)
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    self.player.change_moove(RIGHT)
                if event.key == K_DOWN or event.key == K_s:
                    self.player.change_moove(DOWN)
                if event.key == K_LEFT or event.key == K_a:
                    self.player.change_moove(LEFT)
                if event.key == K_UP or event.key == K_w:
                    self.player.change_moove(UP)

            #другие дейтсвия игрока (other player actions)
                if event.key == K_SPACE:
                    if self.player.state != DEAD:
                        self.player.kill()
                    else:
                        self.player.state = ALIVE
                if event.key == K_z:
                    self.player.skill_list[0].click_check()


            #при отжатии клавиши (when the key is released)
            elif event.type == KEYUP:
                if event.key == K_UP or K_w or K_DOWN or K_s or K_RIGHT or K_d or K_LEFT or K_a:
                    self.player.stop()
                    temp = pygame.key.get_pressed()
                    if temp[275] == 1:
                        self.player.change_moove(RIGHT)
                    if temp[274] == 1:
                        self.player.change_moove(DOWN)
                    if temp[276] == 1:
                        self.player.change_moove(LEFT)
                    if temp[273] == 1:
                        self.player.change_moove(UP)

               #
               # if event.key == K_UP or event.key == K_w:
               #     self.player.mooving[UP] = 0
               # if event.key == K_DOWN or event.key == K_s:
               #     self.player.mooving[DOWN] = 0
               # if event.key == K_RIGHT or event.key == K_d:
               #     self.player.mooving[RIGHT] = 0
               # if event.key == K_LEFT or event.key == K_a:
               #     self.player.mooving[LEFT] = 0
            #для нажатия кнопкой мыши
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in self.buttons:
                        i.click_check(event.pos[0], event.pos[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                [i.unpress() for i in self.buttons if i.pressed == True]

    def add_demon(self, x, y):
        self.mobs.append(Demon(self, x, y, DOWN))
        self.mobs[-1].mooving = [0, 1, 0, 0]

    def render(self):

        #прорисовка всего (drawing of the whole)
        self.screen.blit(self.camera, (0, 0))
        self.camera.blit(self.background, (0, 0))

        [i.render(self.camera) for i in self.corpses]
        self.player.render(self.camera)
        self.player.render_ui(self.screen)
        [i.render(self.camera) for i in self.mobs]
        [i.render(self.camera) for i in self.projective]
        [i.render(self.screen) for i in self.buttons]
        pygame.display.update()

    def moove(self):
        # цикл для передвижениея персонажа, мобов, патронов, всего короче
        if self.player.state != DEAD:
            self.player.moove()
        for i in self.projective:
            i.moove()
        for i in self.mobs:
            if i.state != DEAD:
                i.moove()

    # основной цикл программы (main program cycle)
    def main_loop(self):
        #создаём фоновую музыку в игре (create background music in the game)
        music = pygame.mixer.music.load('music/main_track.mp3')
        pygame.mixer.music.play(-1, 0.0)

        #время регена (regen time)
        pygame.time.set_timer(USEREVENT + 1, 100)
        pygame.time.set_timer(USEREVENT + 2, 100)

        while self.running == True:
            self.timer.tick(60)
            self.moove()
            self.render()
            self.handle_events()



pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
game = Main(screen)
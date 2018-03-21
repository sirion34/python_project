import pygame
from Constants import *
from Player import *
from pygame.locals import *
from Projective import *
from Mob import *

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(self, 'SIRION')
        self.projective = []
        self.mobs = []
        self.background = pygame.image.load('data/background.jpg')
        self.timer = pygame.time.Clock()
        self.running = True
        self.main_loop()



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            #эвент регена (regen event)
            elif event.type == USEREVENT + 1:
                self.player.tick()
            #эвент рандомного передвижения
            elif event.type == USEREVENT + 2:
                self.mobs[0].random_moove()

            #передвижение игрока (player movement)
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    self.player.mooving = [1, 0, 0, 0]
                if event.key == K_DOWN or event.key == K_s:
                    self.player.mooving = [0, 1, 0, 0]
                if event.key == K_LEFT or event.key == K_a:
                    self.player.mooving = [0, 0, 1, 0]
                if event.key == K_UP or event.key == K_w:
                    self.player.mooving = [0, 0, 0, 1]

            #другие дейтсвия игрока (other player actions)
                if event.key == K_SPACE:
                    if self.player.state != DEAD:
                        self.player.die()
                    else:
                        self.player.state = ALIVE
                if event.key == K_z:
                    self.player.shoot_z()


            #при отжатии клавиши (when the key is released)
            elif event.type == KEYUP:
               if event.key == K_UP or event.key == K_w:
                   self.player.mooving[UP] = 0
               if event.key == K_DOWN or event.key == K_s:
                   self.player.mooving[DOWN] = 0
               if event.key == K_RIGHT or event.key == K_d:
                   self.player.mooving[RIGHT] = 0
               if event.key == K_LEFT or event.key == K_a:
                   self.player.mooving[LEFT] = 0

    def add_demon(self, x, y):
        self.mobs.append(Demon(self, x, y, DOWN))

    def render(self):

        #прорисовка всего (drawing of the whole)
        self.screen.blit(self.background,(0,0))
        self.player.render(screen)
        self.player.render_ui(screen)
        for i in self.projective:
            i.render(screen)
        for i in self.mobs:
            i.render(screen)
        pygame.display.flip()

    # основной цикл программы (main program cycle)
    def main_loop(self):

        #создаём фоновую музыку в игре (create background music in the game)
        music = pygame.mixer.music.load('music/main_track.mp3')
        pygame.mixer.music.play(-1, 0.0)

        #время регена (regen time)
        pygame.time.set_timer(USEREVENT + 1, 100)
        pygame.time.set_timer(USEREVENT + 2, 2000)
        self.add_demon(300,250)




        #цикл для передвижениея персонажа (loop for character movement)
        while self.running == True:
            self.timer.tick(60)

            #прописываем, что если ГГ умер, то двигаться он не может (prescribe that if GG died, then he can not move)
            if self.player.state != DEAD:
                self.player.moove()
            for i in self.projective:
                i.moove()
            for i in self.mobs:
                i.moove()
            print(self.projective)
            self.render()
            self.handle_events()



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
game = Main(screen)
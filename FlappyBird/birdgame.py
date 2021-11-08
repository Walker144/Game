import sys
import pygame
import copy
from pygame.locals import *
import random
import string


clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,768))
pygame.init()
TUBESCROLL = -2

FONT = pygame.font.Font('FlappyBird/bird.ttf',32)

def distance(pos1,pos2):
    return ((pos1[0]-pos2[0])**2 + (pos1[1]- pos2[1]) **2)**0.5

class Bird():
    def __init__(self):
        self.y= 500
        self.x = 300
        self.dy = 0
        self.dy2 = 0.4

        self.images = [pygame.transform.scale(pygame.image.load('FlappyBird/flying/frame-1.png'), (50, 50)),pygame.transform.scale(pygame.image.load('FlappyBird/flying/frame-2.png'), (50, 50)),pygame.transform.scale(pygame.image.load('FlappyBird/flying/frame-3.png'), (50, 50)),pygame.transform.scale(pygame.image.load('FlappyBird/flying/frame-4.png'), (50, 50))]

        self.since = 0
        self.ground = False
    def move(self):
        if pygame.mouse.get_pressed()[0]:

                    self.dy = -6


        self.dy += self.dy2

        if self.y < 650:
            self.y += self.dy
        else:
            if self.dy < 0:
                self.y += self.dy
                self.ground = False
            else:
                self.ground = True

    def draw(self):
        if not self.ground:
            self.since = self.since % 60
            if self.since < 15:
                screen.blit(self.images[0], (self.x, self.y))
            elif self.since < 30:
                screen.blit(self.images[1], (self.x, self.y))
            elif self.since < 45:
                screen.blit(self.images[2], (self.x, self.y))
            else:
                screen.blit(self.images[3],(self.x,self.y))
            self.since += 1
        else:

            screen.blit(pygame.transform.rotate((self.images[0]),-10),(self.x,self.y))

class Tube():
    def __init__(self,y1,x):
        self.tube = pygame.image.load('FlappyBird/tube4.png')
        self.tube.set_colorkey((255, 255, 255))
        self.tube.convert_alpha()
        self.x = x

        self.y1 = y1
        self.y2 = y1 - random.randint(200,400)

        self.tube =pygame.transform.scale(self.tube,(100,700))
        self.toptube = pygame.transform.rotate(self.tube,180)
        self.scored = False
    def draw(self):

        screen.blit(self.tube,(self.x,self.y1))
        screen.blit(self.toptube,(self.x,self.y2 - 700 ))
    def move(self):
        self.x += TUBESCROLL

    def checkcollision(self,x,y):
        try:
            pixel = screen.get_at((int(x) + 50 , int(y)))[:3]
        except:
            pixel = (0,0,0)
        if distance([self.x,self.y1], [b.x+25,b.y+25]) < 20:

            return -1
        elif distance([self.x, self.y2], [b.x + 25, b.y + 25]) < 20:

            return -1
        elif distance([self.x + 100, self.y1 ], [b.x + 25, b.y + 25]) < 20:

            return -1
        elif distance([self.x  + 100, self.y2], [b.x + 25, b.y + 25]) < 20:

            return -1

        elif pixel == (0,183,5):
                            print('hitg')
                            return -1





        elif self.x + 100 < b.x and self.scored == False:
            self.scored = True
            return 1
        else:
            return 0



class Background():
    def __init__(self,x):
        self.image = pygame.image.load('FlappyBird/background.png')
        self.x = x
        self.y = 0
    def move(self):
        self.x -= 1
        if self.x == -1024:
            self.x = 2048
    def draw(self):
        screen.blit(self.image,(self.x, 0))

b = Bird()
tubes=  []
for i in range(5):
    tubes.append(Tube(random.randint(100,700),900 + i * 250 ))
score = 0
scoreoffset = 0
balist = [Background(0),Background(1024),Background(2048)]

while True:
    clock.tick(60)
    screen.fill((255,255,255))
    for ba in balist:
        ba.draw()
        ba.move()
    b.move()
    b.draw()

    tubecopy = tubes.copy()
    popped = True

    while popped:
        popped = False
        for i in range(len(tubes)):

            if tubes[i].x < -150:
                tubes[i] = 0
                popped = True

            else:
                tubes[i].move()
                tubes[i].draw()
                delta = tubes[i].checkcollision(b.x, b.y)
                if delta == 1:
                    score += delta
                if delta == -1:
                    print(f'Score: {score}')
                    pygame.quit()
                    sys.exit()

        for tube in range(len(tubes)):
            if tubes[tube] == 0:
                tubes[tube] = Tube(random.randint(100,700),1200)

    tubecopy = tubes.copy()
    for i in range(len(tubes)):
        pass

    TUBESCROLL = -2 + (-0.5 * ((score - scoreoffset) // 5))

    text = FONT.render(f'Score: {score}', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (512,50)
    screen.blit(text, textRect)

    text = FONT.render(f'FPS: {int(clock.get_fps())}', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (900, 50)
    screen.blit(text, textRect)


    pygame.display.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



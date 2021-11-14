import pygame
from pygame.locals import *
import random
import sys
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,768))
pygame.init()



def Collisiondetection(hook,obj):
    if hook.x + 25 > (obj.x + obj.size[0]/2) and hook.x< ((obj.x + 4* obj.size[0]/5)):
        print('hello')

        #print((hook.y + hook.hooksize[0]),(obj.y + obj.size[1]))

        if (hook.y + hook.hooksize[0]) < (obj.y + obj.size[1]) and (hook.y + hook.hooksize[1]) > (obj.y):
            return 1
    else:
        return 0








class Junk():
    def __init__(self,y):
        self.y = y
        self.x = 1200
        self.dx = -3
        self.image = pygame.image.load('assets/junk/1.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image,random.randint(0,360))
        self.size = self.image.get_size()
        self.hashit = 0
        print(self.size)
        self.letgo = False

    def move(self):
        if self.dx == 0:
            self.y = h.y + 15

        if self.y < 100:
            h.holding = False
            return -1

        if self.x < -50:
            return -2


        self.x += self.dx

    def draw(self):
        screen.blit(self.image,(self.x, self.y))
    def collide(self):
        if self.hashit == 0:
            self.hashit = Collisiondetection(h,self)
        if self.hashit == 1:
            if pygame.mouse.get_pressed()[0]:
                self.letgo = True
                self.hashit = 0
                self.dx = -3
                h.holding = False

            if not self.letgo and not h.holding:
                self.dx = 0
                h.holding = True
            elif not h.holding:
                self.hashit = 0
                h.holding = True




class Hook():
    def __init__(self):
        self.x  = 500
        self.y = 100
        self.image = pygame.image.load('assets/hook.png')
        self.image.set_colorkey((255, 255, 255))
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.flip(self.image,True,False)
        self.hooksize = [15,30]
        self.holding = False

    def move(self):
        self.y = pygame.mouse.get_pos()[1]

    def draw(self):
        screen.blit(self.image,(self.x,self.y))









objects = []

objects.append(Junk(random.randint(300,600)))


h = Hook()


score = 0
while True:
    clock.tick(60)

    screen.fill((255,255,255))
    toremove = []
    i = 0

    if random.randint(1,100) > 98:
        objects.append(Junk(random.randint(300,600)))

    for obj in objects:


        obj.collide()
        iscaught = obj.move()
        if iscaught == -1:
            toremove.append(i)
            score += 1
            print(score)
        elif iscaught == -2:
            toremove.append(i)

        obj.draw()
        i += 1
    for i in toremove:
        objects.pop(i)

    h.move()
    h.draw()












    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
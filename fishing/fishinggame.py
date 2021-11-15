import pygame
from pygame.locals import *
import random
import sys
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,768))
pygame.init()



def Collisiondetection(hook,obj):
    rect1 = pygame.Rect(hook.x + 15,hook.y+15,10,30)
    rect2 = pygame.Rect(obj.x,obj.y,obj.size[0],obj.size[1])

    return rect1.colliderect(rect2)








class Junk():
    def __init__(self,y):
        self.y = y
        self.x = 1200
        self.dx = - 1 * random.randint(1,4)
        self.image = pygame.image.load('assets/junk/1.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image,random.randint(0,360))
        self.size = self.image.get_size()
        self.hashit = 0

        self.letgo = False

    def move(self):
        if self.dx == 0 and self.hashit == 1:
            self.y = h.y + 15

        if self.y < 200:
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

            if not h.holding and not self.letgo:
                self.dx = 0

                h.holding = True

            elif h.holding and self.dx != 0:

                self.hashit = 0
                h.holding = True
    def __repr__(self):
        return f'{self.dx,self.hashit}'


class bottle2(Junk):
    def __init__(self,y):
        super(bottle2,self).__init__(y)
        self.image = pygame.image.load('assets/junk/2.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        self.size = self.image.get_size()



class Hook():
    def __init__(self):
        self.x  = 500
        self.y = 100
        self.image = pygame.image.load('assets/hook.png')
        self.image.set_colorkey((255, 255, 255))
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.flip(self.image,True,False)
        self.size = [50,50]
        self.holding = False

    def move(self):
        if pygame.mouse.get_pos()[1] > 100:
            self.y = pygame.mouse.get_pos()[1]
        else:
            self.y = 100
    def draw(self):
        screen.blit(self.image,(self.x,self.y))



class Rope():
    def __init__(self):
        self.x = h.x + 27
        self.top = 50
        self.bottom = h.y
    def draw(self):
        self.bottom = h.y
        pygame.draw.rect(screen,(0,0,0),(self.x, self.top , 0 , self.bottom - self.top + 5))





objects = []


objects.append(Junk(random.randint(300,600)))


h = Hook()
t = Rope()

score = 0
d = 0
while True:
    clock.tick(60)

    screen.fill((255,255,255))

    pygame.draw.rect(screen,(0,0,0),(0,200,1200,0))
    t.draw()
    toremove = []
    i = 0

    if random.randint(1,100) > 98:

        toadd = random.randint(1,2)
        if toadd == 1:
            objects.append(Junk(random.randint(300,600)))
        elif toadd == 2:
            objects.append(bottle2(random.randint(300, 600)))
    '''if d % 60 == 0:
        print(objects)'''
    d += 1
    h.move()
    i = 0

    while i < len(objects):
        obj = objects[i]

        obj.collide()
        iscaught = obj.move()
        if iscaught == -1:
            objects.pop(i)
            score += 1
            print(score)
        elif iscaught == -2:
            objects.pop(i)
            i=0

        obj.draw()
        i += 1

    h.move()
    h.draw()












    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
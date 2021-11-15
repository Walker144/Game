import pygame
from pygame.locals import *
import random
import sys
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,768))
pygame.init()

FONT = pygame.font.Font('assets/COMIC.ttf',32)
BIGFONT = pygame.font.Font('assets/COMIC.ttf',64)
SMALLFONT = pygame.font.Font('assets/COMIC.ttf',20)


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

class bottle3(Junk):
    def __init__(self,y):
        super(bottle3,self).__init__(y)
        self.image = pygame.image.load('assets/junk/3.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        self.size = self.image.get_size()


class fish():

        def __init__(self, y):
            self.y = y
            self.x = 1200
            self.dx = - 1 * random.randint(4, 8)
            self.image = pygame.image.load('assets/fish/fish1.png').convert_alpha()
            self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
            self.size = self.image.get_size()
            self.hashit = 0

            self.letgo = False

        def move(self):
            if self.dx == 0 and self.hashit == 1:
                return -3

            if self.y < 200:
                h.holding = False
                return -1

            if self.x < -50:
                return -2


            self.x += self.dx

        def draw(self):
            screen.blit(self.image, (self.x, self.y))

        def collide(self):
            if self.hashit == 0:
                self.hashit = Collisiondetection(h, self)

            if self.hashit == 1:
                global playing
                playing  = False
        def __repr__(self):
            return f'{self.dx, self.hashit}'


class jellyfish():
    def __init__(self, y):
        self.y = y
        self.x = 1200
        self.dx = - 1 * random.randint(5, 8)
        self.image = pygame.image.load('assets/fish/jellyfish1.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        self.size = self.image.get_size()
        self.hashit = 0

        self.letgo = False

    def move(self):
        if self.dx == 0 and self.hashit == 1:
            return -3

        if self.y < 200:
            h.holding = False
            return -1

        if self.x < -50:
            return -2

        self.x += self.dx

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def collide(self):
        if t.x > self.x and t.x < self.x + self.size[0]:
            if t.bottom > self.y - self.size[1]:
                global playing
                playing = False

    def __repr__(self):
        return f'{self.dx, self.hashit}'






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
        self.top = 100
        self.bottom = h.y
    def draw(self):
        self.bottom = h.y
        pygame.draw.rect(screen,(0,0,0),(self.x, self.top , 2 , self.bottom - self.top + 5))





objects = []


objects.append(Junk(random.randint(300,600)))


h = Hook()
t = Rope()

score = 0
d = 0

hscore = open('assets/highscore.txt','r').read().split(':')




ship = pygame.transform.scale(pygame.image.load('assets/boat.png'),(300,200))
ship.set_colorkey((169,66,66))
ship = ship.convert_alpha()
playing = True
while playing:
    clock.tick(60)


    screen.fill((255,255,255))
    screen.blit(pygame.image.load('assets/background.png'),(0,0))
    screen.blit(ship, (260, 50))

    t.draw()
    toremove = []
    i = 0

    if random.randint(1,100) > 97:

        toadd = random.randint(1,10 + score //3)
        if toadd in [1,2,3]:
            objects.append(Junk(random.randint(300,600)))
        elif toadd in [4,5,6]:
            objects.append(bottle2(random.randint(300, 600)))
        elif toadd in [7,8,9]:
            objects.append(bottle3(random.randint(300, 600)))
        else:
            randfish = random.randint(1, 2 + score // 10)
            if randfish <= 2:
                objects.append(fish(random.randint(300, 600)))
            else:
                objects.append(jellyfish(random.randint(250, 450)))
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

        elif iscaught == -3:
            playing = False

        obj.draw()
        i += 1

    h.move()
    h.draw()

    text = FONT.render(f'Score: {score}', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (512, 50)
    screen.blit(text, textRect)
    text = SMALLFONT.render(f'Highscore: {" - ".join(hscore)}', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (150, 25)
    screen.blit(text, textRect)









    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



if score > int(hscore[1]):
    name = input('New highscore! Enter Name: ')
    doc = open('assets/highscore.txt','w')
    doc.write(f'{name}:{score}')
    print('High score saved')
    doc.close()






while True:
    clock.tick(60)


    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('assets/background.png'), (0, 0))
    screen.blit(ship, (260, 50))

    h.draw()
    t.draw()
    text = BIGFONT.render(f'Game Over', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (512, 325)
    screen.blit(text, textRect)


    text = BIGFONT.render(f' Score: {score}', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (512, 400)
    screen.blit(text, textRect)



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
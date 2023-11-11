import pygame, sys, time, random
from pygame.locals import QUIT

pygame.init()
winWidth = 1000
winHeight = 600
window = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('i am a bad website')


bg=pygame.transform.scale(pygame.image.load("bg2.jpg"), (winWidth,winHeight))
goodslap=[]
for i in range(0,13):
    goodslap.append(pygame.transform.scale(pygame.image.load("god_slap/pixilart-frames/pixil-frame-"+str(i)+".png"), (100,100)))




class Character:
    #sets up character
    def __init__(self):
        self.x = winWidth/2
        self.y = winHeight/2
        self.i =0
        self.frame=0
        self.delay = 0
        self.hp = 10
        self.sprite = [pygame.transform.scale(pygame.image.load("sprite.png"),(100,100)),pygame.transform.scale(pygame.image.load("pixil-frame-0.png"),(100,100)),goodslap]
    #moves character
    def move(self, userinput):
        if userinput[pygame.K_w]:
            self.y-=1

        elif  userinput[pygame.K_s]:
            self.y +=1

        elif  userinput[pygame.K_a]:
            self.x -=1

        elif  userinput[pygame.K_d]:
            self.x +=1

        if userinput[pygame.K_SPACE]:
            self.attack()
            #attack
        if userinput[pygame.K_k] and self.i != 1:
            self.godslap()

    def attack(self):
        self.i = 1
        attacksound.stop()
        attacksound.set_volume(.5)
        attacksound.play()

    def godslap(self):
        self.i=3
        self.frame=0
        goodslappy.stop()
        goodslappy.set_volume(50)
        goodslappy.play()
    #draws character
    def draw(self):
        if self.delay>50:
            self.frame += 1
            if self.frame >= 13:
                self.i = 0
            self.delay = 0
        else:
            self.delay +=1
        if self.i == 3:
            window.blit(goodslap[self.frame], (self.x, self.y))
        else:
            window.blit(self.sprite[self.i], (self.x, self.y))
        if self.hp  <= 0:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        pygame.draw.rect(window,"black",pygame.Rect(self.x-10,self.y-25,104,24))
        pygame.draw.rect(window, "red", pygame.Rect(self.x - 8, self.y - 23, 100*self.hp/10, 20))


#makes pigs
class Pig:
    def __init__(self):
        self.x = winWidth / 2
        self.y = winHeight / 2
        self.i = 0
        self.alive = True
        self.sprite = [pygame.transform.scale(pygame.image.load("redpig.png"), (100, 100)),pygame.transform.scale(pygame.image.load("deth1.png"), (100, 100)),pygame.transform.scale(pygame.image.load("deth2.png"), (100, 100))]
    # makes pigs be damaged by the slap
    def move(self):
        direction = random.randint(0,3)
        if direction == 0:
            if self.x >= 10:
                for i in range(0,10):
                     self.x-=1
                     self.hit()
        elif direction == 1:
            if self.x <= 900:
                for i in range(0, 10):
                    self.x += 1
                    self.hit()
        elif direction == 2:
            if self.y >= 10:
                for i in range(0,10):
                    self.y-=1
                    self.hit()
        elif direction == 3:
            if self.y <= 500:
                for i in range(0, 10):
                    self.y += 1
                    self.hit()


    def hit(self):
        if player.x <= self.x <= player.x+100 and self.alive == True:
            if player.y <= self.y <= player.y + 100:
                if player.i == 1 or player.i ==3:
                    self.alive = False
    def draw(self):
        if self.alive == True:
            if self.i < 3:
                self.move()
                window.blit(self.sprite[self.i], (self.x, self.y))
        elif self.alive== False and self.i>2:
            self.i+=1
            window.blit(self.sprite[self.i], (self.x, self.y))
            pygame.mixer.Sound('')

def collision(bom):
    dist(player.x, player.y, bom.x, bom.y)
    if distance <= 50:
        hp -= 1
        explosionSound.stop()
        explosionSound.set_volume(50)
        explosionSound.play()
        fill(0,0,0)
        textSize(100)
        text("You Lost a life",100,100)

def dist(px,py,bx,by):
    px2 = px + 100
    py2 = py + 100
    bx2 = bx + 100
    by2 = by + 100
    if px <= bx2 <= px2 and py <= by2 <= py2:
        return 1
    return 0


def draw():
    global lives
    #collision(bom)
    window.blit(bg,(0,0))
    player.draw()
    for pig in pigs:
        pig.draw()
    for bom in boms:
        bom.i = dist(player.x,player.y,bom.x,bom.y)
        if dist(player.x,player.y,bom.x,bom.y) == 1:
            player.hp -=0.1
            bom.explosion = True
            explosionSound.stop()
            explosionSound.set_volume(.5)
            explosionSound.play()
        bom.draw()
        if bom.x > 990:
            deleteboms()
            break
            print("bombs deleted")

    pygame.display.flip()


class bom:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.i = 0
        self.explosion = False
        self.sprite = [pygame.transform.scale(pygame.image.load("bom.png"),(100,100)), pygame.transform.scale(pygame.image.load("explosion.png"),(100,100)),]
    def move(self):
        self.x +=1
    def draw(self):
        if self.explosion is False:
            self.i = 0
            self.move()
        else:
            self.i = 1
        window.blit(self.sprite[self.i],(self.x,self.y))

score = 0
#scoreText = pygame.font.SysFont('corbel',35).render(score,True,(0,0,0))
player = Character()
pigs = []
boms = []

for i in range(0,20):
    pigs.append(Pig())
def resetboms():
    print("bombs reset")
    for i in range(0,6):
        boms.append(bom())
        boms[i].y += 100*i
    boms.remove(boms[random.randint(0,5)])
def deleteboms():
    print ("deleteboms()")
    for bom in boms:
        boms.remove(bom)


resetboms()
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1,100)
pygame.mixer.music.set_volume(.2)

attacksound=pygame.mixer.Sound('slap.mp3')
attacksound.set_volume(0)
goodslappy=pygame.mixer.Sound('goodslap21.mp3')
goodslappy.set_volume(10)

explosionSound=pygame.mixer.Sound('bomsound.mp3')
explosionSound.set_volume(10)
delay = 0
while True:
    draw()
    if len(boms) <1:
        resetboms()
    userinput = pygame.key.get_pressed()
    player.move(userinput)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    #print(len(boms))
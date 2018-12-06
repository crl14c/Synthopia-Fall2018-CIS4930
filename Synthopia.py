import pygame
import sys
import random

pygame.init()
pygame.mixer.init()
width = 1300
height = 680
shipfile = "resources/spaceship1.png"
musicfile = "resources/mainmenu.wav"
turretfile = "resources/turret.png"
size = (width, height)

#colors
black = (0, 0, 0)
white = (255, 255, 255)
purple = (175, 0, 175)
green = (0, 255, 0)
grey = (205, 205, 205)
lightblue = (173, 216, 230)
yellow = (255,255,51)


gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Synthopia: Bastion of Scrap')
clock = pygame.time.Clock()


def text_objects(text, font, color=black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def mainscreen():
    main = True
    img = pygame.image.load('resources/space.jpg')
    pygame.mixer.music.load(musicfile)
    pygame.mixer.music.play(loops=-1)
    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(img, (0, 0))
        #Title = pygame.font.Font('')
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRec = text_objects('Synthopia: Bastion of Scrap', largeText, white)
        TextRec.center = (width/2, ((height/2) - 100))
        gameDisplay.blit(TextSurf, TextRec)

        #pygame.draw.rect(gameDisplay, grey, ((width - 150), 25, 100, 50)) for in game settings

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if width - 50 > mouse[0] > (width - 150) and 150 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, lightblue, ((width - 150), 50, 100, 50))
            if click[0] == 1:
                settings()
        else:
            pygame.draw.rect(gameDisplay, grey, ((width - 150), 50, 100, 50))

        if ((width / 2) - 100) > mouse[0] > (width / 2) - 200 and (height/2 + 100) > mouse[1] > (height/2):
            pygame.draw.rect(gameDisplay, lightblue, (((width / 2) - 200), height / 2, 100, 50))
            if click[0] == 1:
                gameloop()
        else:
            pygame.draw.rect(gameDisplay, grey, (((width / 2) - 200), height / 2, 100, 50))

        if ((width / 2) + 200) > mouse[0] > (width / 2) + 100 and (height/2)+100 > mouse[1] > (height/2):
            pygame.draw.rect(gameDisplay, lightblue, (((width / 2) + 100), height / 2, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, grey, (((width / 2) + 100), height / 2, 100, 50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRec = text_objects("Play", smallText, black)
        textRec.center = ((width / 2) - 150, height/2 + 25)
        gameDisplay.blit(textSurf, textRec)
        textSurf, textRec = text_objects("Settings", smallText, black)
        textRec.center = ((width - 100), 75)
        gameDisplay.blit(textSurf, textRec)
        textSurf, textRec = text_objects("Exit", smallText, black )
        textRec.center = ((width / 2) + 150, height / 2 + 25)
        gameDisplay.blit(textSurf, textRec)
        pygame.display.update()


def settings():
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("comicsansms", 50)
    TextSurf, TextRect = text_objects("Settings", largeText, white)
    TextRect.center = ((width / 2), (height / 2 - 150))
    gameDisplay.blit(TextSurf, TextRect)
    img = pygame.image.load('resources/space.jpg')
    gameDisplay.blit(img, (0, 0))

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((width / 2) + 75) > mouse[0] > (width / 2) - 75 and (height/2 + 50) > mouse[1] > (height/2) - 50:
            pygame.draw.rect(gameDisplay, lightblue, (((width / 2) - 75), (height / 2) - 50, 150, 50))
            if click[0] == 1:
                mainscreen()
        else:
            pygame.draw.rect(gameDisplay, grey, (((width / 2) - 75), (height / 2) - 50, 150, 50))

        if ((width / 2) + 50) > mouse[0] > (width / 2) - 50 and (height/2) + 250 > mouse[1] > (height/2) + 150:
            pygame.draw.rect(gameDisplay, lightblue, (((width / 2) - 50), (height / 2) + 150, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, grey, (((width / 2) - 50), (height / 2) + 150, 100, 50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRec = text_objects("Main Menu", smallText)
        textRec.center = ((width / 2), height / 2 - 25)
        gameDisplay.blit(textSurf, textRec)
        textSurf, textRec = text_objects("Exit", smallText)
        textRec.center = (width / 2, height / 2 + 175)
        gameDisplay.blit(textSurf, textRec)
        pygame.display.update()
        clock.tick(15)


def unpause():
    global pause
    pause = False


def paused():
    largeText = pygame.font.SysFont("comicsansms",70)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((width / 2), (height / 2) - 150)
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if ((width / 2) - 100) > mouse[0] > (width / 2) - 200 and (height/2 + 100) > mouse[1] > (height/2):
            pygame.draw.rect(gameDisplay, lightblue, (((width / 2) - 200), height / 2, 100, 50))
            if click[0] == 1:
                break
        else:
            pygame.draw.rect(gameDisplay, grey, (((width / 2) - 200), height / 2, 100, 50))

        if ((width / 2) + 200) > mouse[0] > (width / 2) + 100 and (height/2)+100 > mouse[1] > (height/2):
            pygame.draw.rect(gameDisplay, lightblue, (((width / 2) + 100), height / 2, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, grey, (((width / 2) + 100), height / 2, 100, 50))

        if ((width / 2) + 75) > mouse[0] > (width / 2) - 75 and (height / 2) + 200 > mouse[1] > (height / 2) + 100:
            pygame.draw.rect(gameDisplay, lightblue, ((width / 2) - 75, (height / 2) + 100, 150, 50))
            if click[0] == 1:
                mainscreen()
        else:
            pygame.draw.rect(gameDisplay, grey, ((width / 2) - 75, (height / 2) + 100, 150, 50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRec = text_objects("Unpause", smallText)
        textRec.center = ((width / 2) - 150, height / 2 + 25)
        gameDisplay.blit(textSurf, textRec)
        textSurf, textRec = text_objects("Main Menu", smallText)
        textRec.center = (width / 2, (height / 2) + 125)
        gameDisplay.blit(textSurf, textRec)
        textSurf, textRec = text_objects("Exit", smallText)
        textRec.center = ((width / 2) + 150, height / 2 + 25)
        gameDisplay.blit(textSurf, textRec)
        pygame.display.update()
        clock.tick(15)


class Turret(pygame.sprite.Sprite):
    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(turretfile)
        self.rect = self.image.get_rect()
        self.rect.x = w - 5
        self.rect.y = h - 90


def turret(click, mouse, w, h, p, st, m, t):
    if w + 50 > mouse[0] > w and h + 50 > mouse[1] > h:
        pygame.draw.rect(gameDisplay, purple, (w, h, 50, 50))
        if click[0] == 1 and p and m >= 250 and st != 1:
            turret2 = Turret(w, h)
            m = m - 250
            t.add(turret2)
            return 1, m, t
        if st == 1:
            return 1, m, t
        else:
            return 0, m, t

    else:
        if st == 1:
            return 1, m, t
        else:
            pygame.draw.rect(gameDisplay, pygame.Color(203, 132, 128, 1), (w, h, 50, 50))
            return 0, m, t


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = random.randint(75, 150)
        self.image = pygame.image.load(shipfile)
        self.image = pygame.transform.rotate(self.image,180)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, 0)
        self.movement = 2

    def update(self):
        self.rect.x += self.movement
        self.rect.y += .2
        if self.rect.right > width:
            self.movement = self.movement*-1  -1

        if self.rect.left < 0:
            self.movement = 1 + self.movement*-1


def gameloop():
    global pause
    imgback= pygame.image.load('resources/earth.png')
    run = True
    placingTurret = False
    start = True
    money = 600
    health = 1000
    start_ticks = pygame.time.get_ticks()
    font = pygame.font.SysFont('Consolas', 30)
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    imgTurret = pygame.image.load('resources/turret.png')
    enemies = pygame.sprite.Group()
    turretGroup = pygame.sprite.Group()

    if enemies.empty:
        ship = Ship()
        enemies.add(ship)

    while run:
        seconds = 60 - (pygame.time.get_ticks() - start_ticks) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    global pause
                    pause = True
                    paused()

        gameDisplay.blit(imgback, (0, -450))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        '''pause button box made here'''
        if width - 50 > mouse[0] > (width - 150) and 150 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, lightblue, ((width - 150), 50, 100, 50))
            if click[0] == 1:
                pause = True
                paused()
        else:
            pygame.draw.rect(gameDisplay, grey, ((width - 150), 50, 100, 50))
        '''Click to place Turret'''
        if 100 > mouse[0] > 0 and 450 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, purple, (0, 50, 100, 400))
            if click[0] == 1:
                if not placingTurret:
                    placingTurret = True
                elif placingTurret:
                    placingTurret = False

        else:
            pygame.draw.rect(gameDisplay, grey, (0, 50, 100, 400))

        gameDisplay.blit(imgTurret, (0, 200))
        '''Turret places being drawn'''
        status[0], money, turretGroup = turret(click, mouse, 75, height - 75, placingTurret, status[0], money, turretGroup)
        status[1], money, turretGroup = turret(click, mouse, 175, height - 175, placingTurret, status[1], money, turretGroup)
        status[2], money, turretGroup = turret(click, mouse, 275, height - 75, placingTurret, status[2], money, turretGroup)
        status[3], money, turretGroup = turret(click, mouse, 375, height - 175, placingTurret, status[3], money, turretGroup)
        status[4], money, turretGroup = turret(click, mouse, 475, height - 75, placingTurret, status[4], money, turretGroup)
        status[5], money, turretGroup = turret(click, mouse, 562.5, height - 175, placingTurret, status[5], money, turretGroup)
        status[6], money, turretGroup = turret(click, mouse, 650, height - 75, placingTurret, status[6], money, turretGroup)
        status[7], money, turretGroup = turret(click, mouse, 737.5, height - 175, placingTurret, status[7], money, turretGroup)
        status[8], money, turretGroup = turret(click, mouse, 825, height - 75, placingTurret, status[8], money, turretGroup)
        status[9], money, turretGroup = turret(click, mouse, 912.5, height - 175, placingTurret, status[9], money, turretGroup)
        status[10], money, turretGroup = turret(click, mouse, 1000, height - 75, placingTurret, status[10], money, turretGroup)
        status[11], money, turretGroup = turret(click, mouse, 1075, height - 175, placingTurret, status[11], money, turretGroup)
        status[12], money, turretGroup = turret(click, mouse, 1150, height - 75, placingTurret, status[12], money, turretGroup)

        textSurf, textRec = text_objects("Pause", smallText, black)
        textRec.center = ((width - 100), 75)
        textSurf2, textRec2 = text_objects(str(round(seconds)),font, white)
        textRec2.center = ((width-100), 200)
        textSurfMoney, textRecMoney = text_objects(str(money) + "$", smallText, yellow)
        textRecMoney.center = (30, height - 650)
        textSurfHealth, textRecHealth = text_objects("Health: " + str(health), smallText, green)
        textRecHealth.center = ((width - 100), 30)
        textSurf3, textRec3 = text_objects("You have 60 seconds to place your turrets.", font, white)
        textRec3.center = ((width-650), 200)
        textSurf4, textRec4 = text_objects("Turret Place Active", smallText, white)
        textRec4.center = ((width/2), height/2)
        textSurf5, textRec5 = text_objects("Place", smallText, black)
        textRec5.center = (50, 100)
        textSurf6, textRec6 = text_objects("a", smallText, black)
        textRec6.center = (50, 120)
        textSurf7, textRec7 = text_objects("Turret", smallText, black)
        textRec7.center = (50, 140)
        textSurf8, textRec8 = text_objects("Cost", smallText, black)
        textRec8.center = (50, 380)
        textSurf9, textRec9 = text_objects("250$", smallText, black)
        textRec9.center = (50, 400)
        gameDisplay.blit(textSurf, textRec)

        gameDisplay.blit(textSurf9, textRec9)
        gameDisplay.blit(textSurf8, textRec8)
        gameDisplay.blit(textSurf7, textRec7)
        gameDisplay.blit(textSurf6, textRec6)
        gameDisplay.blit(textSurf5, textRec5)
        if seconds > 0:
            gameDisplay.blit(textSurf2, textRec2)
        elif seconds <=0:
            start = False

        if seconds > 30:
            gameDisplay.blit(textSurf3,textRec3)

        if placingTurret:
            gameDisplay.blit(textSurf4, textRec4)

        gameDisplay.blit(textSurfMoney, textRecMoney)
        gameDisplay.blit(textSurfHealth, textRecHealth)

        shipfile = "spaceship1.png"
        #if start == False:

        turretGroup.draw(gameDisplay)
        enemies.draw(gameDisplay)
        enemies.update()
        pygame.display.update()

all_fonts = pygame.font.get_fonts()
mainscreen()
gameloop()
pygame.quit()
quit()
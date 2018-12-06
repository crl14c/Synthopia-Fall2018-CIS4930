import pygame
import sys

pygame.init()
pygame.mixer.init()
width = 1300
height = 680
musicfile = "resources/mainmenu.wav"
size = (width, height)

#colors
black = (0, 0, 0)
white = (255, 255, 255)
purple = (175, 0, 175)
green = (0, 255, 0)
grey = (205, 205, 205)
lightblue = (173, 216, 230)


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
    TextSurf, TextRect = text_objects("Settings", largeText)
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


def placeTurret(w, h):
    #function to the turret in the turret place
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRec = text_objects("Exit", smallText, white)
    textRec.center = ((width / 2) + 150, height / 2 + 25)
    gameDisplay.blit(textSurf, textRec)
    imgTurret = pygame.image.load('resources/turret.png')
    gameDisplay.blit(imgTurret, (w - 5, h - 90))


def turret(click, mouse, w, h, p, st):
    if w + 50 > mouse[0] > w and h + 50 > mouse[1] > h:
        pygame.draw.rect(gameDisplay, purple, (w, h, 50, 50))
        if click[0] == 1 and p:
            #placeTurret(w, h)
            return 1
        if st == 1:
            return 1
        else:
            return 0

    else:
        if st == 1:
            return 1
        else:
            pygame.draw.rect(gameDisplay, pygame.Color(203, 132, 128, 1), (w, h, 50, 50))
            return 0


def gameloop():
    imgback= pygame.image.load('resources/earth.png')
    run = True
    placingTurret = False
    start = True
    money = 0
    health=1000
    start_ticks = pygame.time.get_ticks()
    font = pygame.font.SysFont('Consolas', 30)
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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
        if 50 > mouse[0] > 0 and 450 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, green, (0, 50, 50, 400))
            if click[0] == 1:
                if not placingTurret:
                    placingTurret = True
                elif placingTurret:
                    placingTurret = False

        else:
            pygame.draw.rect(gameDisplay, grey, (0, 50, 50, 400))
        '''Turret places being drawn'''
        if status[0] != 1:
            status[0] = turret(click, mouse, 75, height - 75, placingTurret, status[0])
        if status[1] != 1:
            status[1] = turret(click, mouse, 175, height - 175, placingTurret, status[1])
        if status[2] != 1:
            status[2] = turret(click, mouse, 275, height - 75, placingTurret, status[2])
        if status[3] != 1:
            status[3] = turret(click, mouse, 375, height - 175, placingTurret, status[3])
        if status[4] != 1:
            status[4] = turret(click, mouse, 475, height - 75, placingTurret, status[4])
        if status[5] != 1:
            status[5] = turret(click, mouse, 562.5, height - 175, placingTurret, status[5])
        if status[6] != 1:
            status[6] = turret(click, mouse, 650, height - 75, placingTurret, status[6])
        if status[7] != 1:
            status[7] = turret(click, mouse, 737.5, height - 175, placingTurret, status[7])
        if status[8] != 1:
            status[8] = turret(click, mouse, 825, height - 75, placingTurret, status[8])
        if status[9] != 1:
            status[9] = turret(click, mouse, 912.5, height - 175, placingTurret, status[9])
        if status[10] != 1:
            status[10] = turret(click, mouse, 1000, height - 75, placingTurret, status[10])
        if status[11] != 1:
            status[11] = turret(click, mouse, 1075, height - 175, placingTurret, status[11])
        if status[12] != 1:
            status[12] = turret(click, mouse, 1150, height - 75, placingTurret, status[12])

        if status[0] == 1:
            placeTurret(75, height - 75)
        if status[1] == 1:
            placeTurret(175, height - 175)
        if status[2] == 1:
            placeTurret(275, height - 75)
        if status[3] == 1:
            placeTurret(375, height - 175)
        if status[4] == 1:
            placeTurret(475, height - 75)
        if status[5] == 1:
            placeTurret(562.5, height - 175)
        if status[6] == 1:
            placeTurret(650, height - 75)
        if status[7] == 1:
            placeTurret(737.5, height - 175)
        if status[8] == 1:
            placeTurret(825, height - 75)
        if status[9] == 1:
            placeTurret(912.5, height - 175)
        if status[10] == 1:
            placeTurret(1000, height - 75)
        if status[11] == 1:
            placeTurret(1075, height - 175)
        if status[12] == 1:
            placeTurret(1150, height - 75)

        textSurf, textRec = text_objects("Pause", smallText, black)
        textRec.center = ((width - 100), 75)
        textSurf2, textRec2 = text_objects(str(round(seconds)),font, white)
        textRec2.center = ((width-100), 200)
        textSurfMoney, textRecMoney = text_objects(str(money) + "$", smallText, white)
        textRecMoney.center = ((width/2), height - 650)
        textSurf3, textRec3 = text_objects("You have 60 seconds to place your turrets.", font, white)
        textRec3.center = ((width-650), 200)
        textSurf4, textRec4 = text_objects("Turret Place Active", smallText, white)
        textRec4.center = ((width/2), height/2)
        gameDisplay.blit(textSurf, textRec)
        if seconds > 0:
            gameDisplay.blit(textSurf2, textRec2)
        elif seconds <=0:
            start = False

        if seconds > 30:
            gameDisplay.blit(textSurf3,textRec3)

        if placingTurret:
            gameDisplay.blit(textSurf4, textRec4)

        gameDisplay.blit(textSurfMoney, textRecMoney)
        pygame.display.update()


all_fonts = pygame.font.get_fonts()
mainscreen()
gameloop()
pygame.quit()
quit()
import pygame
import sys

pygame.init()
width = 1300
height = 680
size = (width, height)

#colors
black = (0, 0, 0)
white = (255, 255, 255)
purple =(128, 0, 128)
green = (0, 255, 0)
grey = (128, 128, 128)


gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Synthopia: Bastion of Scrap')
clock = pygame.time.Clock()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def mainscreen():
    main = True
    while main:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        #Title = pygame.font.Font('')
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRec = text_objects('Synthopia: Bastion of Scrap', largeText)
        TextRec.center = (width/2, ((height/2) - 100))
        gameDisplay.blit(TextSurf, TextRec)
        pygame.draw.rect(gameDisplay, grey, (((width/2)-50), height/2,100,50))
        #pygame.draw.rect(gameDisplay, grey, ((width - 150), 25, 100, 50)) for in game settings
        pygame.draw.rect(gameDisplay, grey, (((width / 2) - 200), height / 2, 100, 50))
        pygame.draw.rect(gameDisplay, grey, (((width / 2) + 100), height / 2, 100, 50))
        pygame.display.update()


def gameloop():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(60)


all_fonts = pygame.font.get_fonts()
mainscreen()
gameloop()
pygame.quit()
quit()
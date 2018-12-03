import pygame

from PyQt5 import QtWidgets, QtCore, QtGui
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Game():
    def __init__(self):
        pygame.init()
        self.game_init()

    def game_init(self):
        self.size = 0

    #pygame main loop here
    def loop(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        return False


class Data:
    def __init__(self):
        self.option = 0


class MainWindow(QtWidgets.QMainWindow, Data):
    def __init__(self, game):
        QtWidgets.QMainWindow.__init__(self)
        super().__init__()
        self.fullscreen = 0
        self.option = 0
        self.setup()
        self.init_pygame(game)

    def setup(self):
        self.setWindowTitle('Synthopia: Bastion of Scrap')
        self.buttons()
        if self.fullscreen == 0:
            self.showMaximized()
        else:
            self.showFullScreen()

    def init_pygame(self, game):
        self.game = game
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)

    def pygame_loop(self):
        if self.game.loop(self):
            self.close()

    def buttons(self):
        print(self.option)
        self.settings = QtWidgets.QPushButton("Settings", self)
        self.settings.move(1250, 10)
        self.exit = QtWidgets.QPushButton("Exit", self)
        self.exit.move(600, 400)
        self.play = QtWidgets.QPushButton("Play", self)
        self.play.move(600, 350)
        self.exitsettings = QtWidgets.QPushButton("Exit Settings", self)
        self.exitsettings.move(1250, 50)
        if self.option == 0:
            self.exitsettings.setVisible(False)
            self.settings.setVisible(True)
            self.exit.setVisible(True)
            self.play.setVisible(True)
            self.settings.clicked.connect(self.settingsOpen)
            self.exit.clicked.connect(self.close)
            self.play.clicked.connect(self.playGame)
        if self.option == 1:
            print("asdasdasdasda")
            self.exitsettings.setVisible(True)
            self.exit.setVisible(False)
            self.exitsettings.clicked.connect(self.backToMain)

    def settingsOpen(self):
        self.option = 1
        self.buttons()
        self.setup()


    def backToMain(self):
        self.option = 0
        self.buttons()
        self.setup()

    def playGame(self):
        self.option = 2
        self.buttons()
        self.setup()


class DrawImage(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)

    def paintEvent(self, event):
        qp = QtGui.QPainter()

        qp.end()


if __name__ == "__main__":
    game = Game()
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow(game)
    app.exec_()

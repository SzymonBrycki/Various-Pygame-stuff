# 1 - importowanie pakietów

import pygame
from pygame.locals import *
import sys
import random
from Ball import *
from SimpleText import *
from SimpleButton import *

# 2 - definiowanie stałych

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMER_PER_SECOND = 30

# 3 - inicjalizacja pygame

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - wczytywanie zasobów

# 5 - inicjalizacja zmiennych

oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (60, 20),
                              "Liczba pętli wykonanych przez program: ", WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), "", WHITE)
oRestartButton = SimpleButton(window, (280, 60),
                                    "images/restartUp.png", 
                                    "images/restartDown.png")

frameCounter = 0

# 6 - nieskończona pętla

while True:

    #7 sprawdzanie zdarzeńi i ich obsługa

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):
            frameCounter = 0

    # 8 - wykonywanie zdarzeń dla klatki

    oBall.update()
    frameCounter = frameCounter +1
    oFrameCountDisplay.setValue(str(frameCounter))

    # 9 - usunięcie zawartości okna

    window.fill(BLACK)

    # 10 - wyświetlenie wszystkich elementów okna

    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # 11 - auktualnienie okna

    pygame.display.update()

    # FPS

    clock.tick(FRAMER_PER_SECOND)

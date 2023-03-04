# 1 - importowanie pakietów

import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# 2 - definiowanie stałych

GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# 3 - inicjalizacja środowiska pygame

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - wczytywanie zasobów

# 5 - inicjalizacja zmiennych

oButton = SimpleButton(window, (150, 30),
                        "images/buttonUp.png",
                        "images/buttonDown.png")

# 6 - pętla działająca w nieskończoność

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButton.handleEvent(event):
            print("Użytkownik kliknął przycisk")

    window.fill(GRAY)

    oButton.draw()
    
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)



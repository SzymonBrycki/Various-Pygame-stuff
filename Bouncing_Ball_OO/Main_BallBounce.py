# 1 - importowanie pakietów

import pygame
from pygame.locals import *
import sys
import random
from Ball import *

# 2 - definiowanie stałych

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - inicjalizacja pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - wczytywanie zasobów: obrazy, dźwięki itp.

# 5 - inicjalizacja zmiennych

oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# 6 - pętla działająca w nieskończoność

while True:

    # 7 - sprawdzanie pdo kątem zdarzeń i ich obsługa

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - wykonywanie zdarzeń w klatkach

    oBall.update()

    # 9 - usunięcie zawartości okna

    window.fill(BLACK)

    # 10 - wyświetlenie wszystkich elelemtnow okna

    oBall.draw()

    # 11 - auktualnienie okna

    pygame.display.update()

    # 12 - niewielkie spowolnienei całości

    clock.tick(FRAMES_PER_SECOND)



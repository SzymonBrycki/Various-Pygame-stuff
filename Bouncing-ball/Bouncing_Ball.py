# 1 -importowanie pakietów

import pygame
from pygame.locals import *
import sys
import random

# 2 - stałe

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# 3 - inicjalizacja środowiska pygame

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 wczytywanie zasobów - obrazy, dźwięki itp.

ballImage = pygame.image.load("IMG/ball.png")

# 5 - Inicjalizacja zmiennych

MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - nieskończona pętla

while True:
    
    # 7 - zdarzenia i ich obsługa

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - wykonywanie akcji dla "danej klatki"
    
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed #ruch w odwrotnym kierunku

    if (ballY <0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed #ruch w odwrotnym kierunku

    ballX = ballX + xSpeed
    ballY = ballY + ySpeed

    # 9 - usunięcie zawartości okna

    window.fill(BLACK)

    # 10 - wyświetlenie wszystkich elementó okna

    window.blit(ballImage, (ballX, ballY))

    # 11 - auktualnienie okna

    pygame.display.update()
    
    # 12 - niewielkie spowolnienie całości

    clock.tick(FRAMES_PER_SECOND)
       
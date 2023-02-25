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
bounceSound = pygame.mixer.Sound("SOUND/boing.wav")
pygame.mixer.music.load("SOUND/background.mp3")
pygame.mixer.music.play(-1, 0.0)

# 5 - Inicjalizacja zmiennych

ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
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
    
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed
        bounceSound.play()

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed
        bounceSound.play()

    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - usunięcie zawartości okna

    window.fill(BLACK)

    # 10 - wyświetlenie wszystkich elementó okna

    window.blit(ballImage, ballRect)

    # 11 - auktualnienie okna

    pygame.display.update()
    
    # 12 - niewielkie spowolnienie całości

    clock.tick(FRAMES_PER_SECOND)
       
import pygame
from pygame.locals import *

class SimpleButton():
    STATE_IDLE = "idle"
    STATE_ARMED = "armed"
    STATE_DISARMED = "disarmed"

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        # prostokąt ograniczający przycisk

        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, eventObj):
        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False
        
        eventPointinButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointinButtonRect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (eventObj.type == MOUSEBUTTONUP) and eventPointinButtonRect:
                self.state = SimpleButton.STATE_IDLE
                return True
            if (eventObj.type == MOUSEMOTION) and (not eventPointinButtonRect):
                self.state = SimpleButton.STATE_DISARMED
        elif self.state == SimpleButton.STATE_DISARMED:
            if eventPointinButtonRect:
                self.state - SimpleButton.STATE_ARMED
            elif eventObj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE
        
        return False
    
    def draw(self):
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)
        
        else:
            self.window.blit(self.surfaceUp, self.loc)

'''
oButton = SimpleButton(window, (150, 30),
                       "images/buttonUp.png",
                       "images/buttonDown.png")
'''
import pygame
from pygame.locals import *

import sys
import os

#display surface
WIDTH, HEIGHT = 1280, 720
HALFWIDTH, HALFHEIGH = WIDTH / 2, WIDTH / 2
AREA = WIDTH * HEIGHT
SCROLLSPEED = 2


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN
                                  and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


os.environ['SDL_VIDEO_WINDOW_POS'] = "1200, 500"

# game constants
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flowsurfer")
FPS = 60

background = pygame.image.load("assets/shittywater.png").convert()
bg_pos = 0

#gameloop
while True:
    events()

    rel_bg_pos = bg_pos % background.get_rect().width

    DS.blit(background, (rel_bg_pos - background.get_rect().width, 0))

    if rel_bg_pos < WIDTH:
        DS.blit(background, (rel_bg_pos, 0))

    bg_pos -= SCROLLSPEED

    pygame.display.update()
    CLOCK.tick(FPS)
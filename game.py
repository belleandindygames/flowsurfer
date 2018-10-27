import pygame
from pygame.locals import *

import sys
import os

# display surface
WIDTH, HEIGHT = 1280, 720
HALFWIDTH, HALFHEIGH = WIDTH / 2, WIDTH / 2
AREA = WIDTH * HEIGHT
SCROLLSPEED = 2


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


os.environ["SDL_VIDEO_WINDOW_POS"] = "1200, 500"
score = 0
timer = 0
timer_milli = 0
millis = 0
# game constants
pygame.init()
pygame.font.init()
score_font = pygame.font.SysFont("Arial", 60, bold=1)

CLOCK = pygame.time.Clock()


DS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flowsurfer")
FPS = 60

background = pygame.image.load("assets/shittywater.png").convert()
bg_pos = 0


# gameloop
while True:
    score_textsurface = score_font.render(f"Score: {score}", False, (233, 233, 115))
    timer_textsurface = score_font.render(
        f"Time: {str(timer).zfill(2)}.{str(timer_milli).zfill(2)}",
        False,
        (233, 233, 115),
    )

    events()

    rel_bg_pos = bg_pos % background.get_rect().width

    DS.blit(background, (rel_bg_pos - background.get_rect().width, 0))

    if rel_bg_pos < WIDTH:
        DS.blit(background, (rel_bg_pos, 0))
    DS.blit(score_textsurface, (2, 2))
    DS.blit(timer_textsurface, (WIDTH - 280, 2))
    bg_pos -= SCROLLSPEED

    pygame.display.update()

    ## set max framerate
    time_this_frame = CLOCK.tick(FPS)

    ## update timer
    millis += time_this_frame
    timer_milli = round((millis % 1000) / 10)
    timer = millis // 1000


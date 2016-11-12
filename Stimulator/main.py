import pygame
import sys
from constants import *
from pygame.locals import *

current_state = ''


def quit_game():
    pygame.quit()
    sys.exit()


def switch_state(new_state):
    global current_state

    current_state = __import__(new_state)
    current_state.init()

if __name__ == '__main__':

    pygame.init()

    flags = SRCALPHA | DOUBLEBUF

    screen = pygame.display.set_mode((var.screen_w, var.screen_h), flags)
    clock = pygame.time.Clock()
    ms = clock.tick(var.fps)

    switch_state('ingame')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            else:
                current_state.on_event(event)
        current_state.update()
        current_state.draw(screen)

        pygame.display.flip()

        ms = clock.tick(var.fps)

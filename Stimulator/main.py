import pygame
import sys
from constants import *
from pygame.locals import *

current_state = ''
cam_position = [100, 100]

def quit_game():
    pygame.quit()
    sys.exit()


def switch_state(new_state):
    global current_state

    current_state = __import__(new_state)
    current_state.init()

if __name__ == '__main__':

    pygame.init()

    flags = pygame.SRCALPHA | pygame.DOUBLEBUF

    screen = pygame.display.set_mode((screen_w, screen_h), flags)
    clock = pygame.time.Clock()
    ms = clock.tick(fps)

    switch_state('intro')

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                else:
                    current_state.on_event(event)

            current_state.update()
            current_state.draw(screen, cam_position)

            pygame.display.flip()

            ms = clock.tick(fps)
        except State_switcher as e:
            switch_state(e.value)
import player
from constants import *
import pygame
import map

cam_position = [100, 100]

def init():
    global player_obj, player_icon


    player_obj = player.Player(100, 200)
    gamemusic = pygame.mixer.music.load("gamesound.wav")
    pygame.mixer.music.play(-1)

def on_event(event):
    player_obj.on_event(event)


def update():
    player_obj.update()
    cam_position[0] = player_obj.x - screen_w/2
    cam_position[1] = player_obj.y - screen_h/2
    # print(cam_position, player_obj.x, player_obj.y)


def draw(screen):
    screen.fill((255, 255, 255))

    map.draw(screen, cam_position)
    player_obj.draw(screen)
import player
from constants import *
import pygame
import map
import enemy

cam_position = [0, 0]


def init():
    global player_obj, player_icon, enemy_icon, enemy_obj
    enemy_icon = pygame.image.load("Kera.png")
    player_icon = pygame.image.load("player.png")
    player_obj = player.Player(100, 650)
    enemy_obj = enemy.Enemy(300, 2020, enemy_icon)
    gamemusic = pygame.mixer.music.load("gamesound.wav")
    pygame.mixer.music.play(-1)
    global pause
    pause = False


def on_event(event):
    global pause
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_m:
            if not pause:
                pygame.mixer.music.pause()
                pause = True
            else:
                pygame.mixer.music.unpause()
                pause = False

    player_obj.on_event(event)


def update():
    player_obj.update(map.get_rect_list())
    enemy_obj.update(player_obj, map.map1_data)
    cam_position[0] = player_obj.x - screen_w/2 + player_obj.rect.w/2
    cam_position[1] = player_obj.y - screen_h/2 + player_obj.rect.h/2
    # print(cam_position, player_obj.x, player_obj.y)


def draw(screen):
    screen.fill((255, 255, 255))

    map.draw(screen, cam_position)
    enemy_obj.draw(screen, cam_position)
    player_obj.draw(screen, cam_position)
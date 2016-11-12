import player
import constants
import pygame


def init():
    global player_obj

    player_icon = pygame.image.load("player.jpg")
    player_obj = player.Player(100, 200, player_icon)


def on_event(event):
    player_obj.on_event(event)


def update():
    player_obj.update()


def draw(screen):
    screen.fill((0, 0, 0))
    player_obj.draw(screen)
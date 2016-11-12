import player
import constants

def init():
    
    pass
def on_event(event):
    player.on_event(event)

def update():
    player.update()

def draw(screen):
    screen.fill((0, 0, 0))
    player.draw(screen)
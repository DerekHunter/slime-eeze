import pyglet
from pyglet.window import key
from pyglet.window import mouse

from Game import *

window = pyglet.window.Window(1920, 1080, fullscreen=True)

game = Game(window)

@window.event
def on_key_press(symbol, modifiers):
    return game.KeyPress(symbol)

@window.event
def on_key_release(symbol, modifiers):
    return game.KeyUp(symbol)

@window.event
def on_mouse_press(x, y, button, modifiers):
    game.MouseClick(x, y, button)

@window.event
def on_draw():
    game.onDraw()

def update(dt):
    game.update(dt)

pyglet.clock.schedule_interval(update, .033)
pyglet.app.run()
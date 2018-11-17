import pyglet

from AssetManager import *

class Player:

  def __init__(self, batch, x, y):
    self.group = pyglet.graphics.OrderedGroup(3)
    self.batch = batch
    

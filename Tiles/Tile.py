import pyglet

class Tile:

  def __init__(self, batch, x, y, tileImg):
    self.group = pyglet.graphics.OrderedGroup(4)
    self.batch = batch
    self.sprite = pyglet.sprite.Sprite(tileImg, batch=self.batch, group=self.group)
    self.sprite.x = x*128
    self.sprite.y = 1080-y*128
    self.x = x*128
    self.y = 1080-y*128

  def update(self, dt, cameraOffset):
    self.sprite.x = self.x - cameraOffset
    pass
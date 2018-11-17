import pyglet
from AssetManager import *
class MainScreen:

  def __init__ (self, window, screenManager):
    print ("Creating Main Screen ")
    self.window = window
    self.batch = pyglet.graphics.Batch()
    self.screenManager = screenManager
    self.MenuBackgroundAnimation = AssetManager.getInstance().MenuBackground
    self.MenuWords = AssetManager.getInstance().MenuWords

    self.MenuBackgroundSprite = pyglet.sprite.Sprite(self.MenuBackgroundAnimation, batch=self.batch, group=pyglet.graphics.OrderedGroup(0))
    self.MenuWords = pyglet.sprite.Sprite(self.MenuWords, batch=self.batch, group=pyglet.graphics.OrderedGroup(1))

  def KeyPress(self, key):
    pass

  def KeyUp(self, key):
    pass

  def MouseClick(self, x, y, button):
    print(x,y)
    if x > 819 and x < 1102 and y < 644 and y > 544:
      self.screenManager.SetScreen("LevelOne")
    if x > 733 and x < 1190 and y < 500 and y > 380:
      print("Settings")
    if x > 850 and x < 1079 and y < 331 and y > 235:
      print("Quit")
  
  def onDraw(self):
    self.window.clear()
    self.batch.draw()

  def update(self, dt):
    pass
from ScreenManager import *
from AssetManager import *

class Game:

  def __init__ (self, window):
    print("Creating Game")
    self.window = window
    self.ScreenManager = ScreenManager(window)
    self.ScreenManager.SetScreen("Menu")

  def KeyPress(self, key):
    print("Key Pressed: ", str(key))
    return self.ScreenManager.KeyPress(key)

  def MouseClick(self, x, y, button):
    print("Mouse Click: ", str(button))
    self.ScreenManager.MouseClick(x,y,button)
  
  def onDraw(self):
    self.ScreenManager.onDraw()
    pass

  def update(self, dt):
    self.ScreenManager.update(dt)
    pass
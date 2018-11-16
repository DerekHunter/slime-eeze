from ScreenManager import *

class Game:

  def __init__ (self, window):
    print("Creating Game")
    self.window = window
    self.ScreenManager = ScreenManager(window)
    pass

  def KeyPress(self, key):
    print("Key Pressed: ", str(key))
    pass

  def MouseClick(self, x, y, button):
    print("Mouse Click: ", str(button))
    pass
  
  def onDraw(self):
    self.ScreenManager.onDraw()
    pass

  def update(self, dt):
    self.ScreenManager.update(dt)
    pass
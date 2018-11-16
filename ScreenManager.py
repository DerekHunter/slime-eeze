from MainScreen import *

class ScreenManager:

  def __init__(self, window):
    print("Creating Screen Manager")
    self.window = window
    self.MainScreen = MainScreen(window)
  
  def KeyPress(self, key):
    pass

  def MouseClick(self, x, y, button):
    pass
  
  def onDraw(self):
    self.MainScreen.onDraw()
    pass

  def update(self, dt):
    self.MainScreen.update(dt)
    pass

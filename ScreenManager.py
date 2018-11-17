from MainScreen import *
from LevelOne import *
from LevelTwo import *
from LevelThree import *

class ScreenManager:

  def __init__(self, window):
    print("Creating Screen Manager")
    self.window = window

  def SetScreen(self, screen):
    if screen == "Menu":
      print("Setting Screen Menu")
      self.currentScreen = MainScreen(self.window, self)
    elif screen == "LevelOne":
      self.currentScreen = LevelOne(self.window, self)
    elif screen == "LevelTwo":
      print("Setting Screen L2")
      self.currentScreen = LevelTwo(self.window, self)
    elif screen == "LevelThree":
      print("Setting Screen L3")
      self.currentScreen = LevelThree(self.window, self)


  def KeyPress(self, key):
    self.currentScreen.KeyPress(key)

  def MouseClick(self, x, y, button):
    self.currentScreen.MouseClick(x, y, button)
  
  def onDraw(self):
    self.currentScreen.onDraw()

  def update(self, dt):
    self.currentScreen.update(dt)
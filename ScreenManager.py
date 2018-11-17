from MainScreen import *
from PauseScreen import *
from Levels.LevelOne import *
from Levels.LevelTwo import *
from Levels.LevelThree import *


class ScreenManager:

  def __init__(self, window):
    print("Creating Screen Manager")
    self.window = window
    self.paused = False
    self.PauseScreen = PauseScreen(self.window, self)

  def SetScreen(self, screen):
    if screen == "Menu":
      print("Setting Screen Menu")
      self.currentScreen = MainScreen(self.window, self)
      self.currentScreenId = "Menu"
    elif screen == "LevelOne":
      self.currentScreen = LevelOne(self.window, self)
      self.currentScreenId = "LevelOne"
    elif screen == "LevelTwo":
      print("Setting Screen L2")
      self.currentScreen = LevelTwo(self.window, self)
      self.currentScreenId = "LevelTwo"
    elif screen == "LevelThree":
      print("Setting Screen L3")
      self.currentScreen = LevelThree(self.window, self)
      self.currentScreenId = "LevelThree"

  def KeyPress(self, key):
    if key == pyglet.window.key.ESCAPE:
      if self.paused:
        print("Unpausing")
        self.paused = False
        return pyglet.event.EVENT_HANDLED
      elif self.currentScreenId != "Menu":
        print("Pausing")
        self.paused = True
        return pyglet.event.EVENT_HANDLED
    else:
      self.currentScreen.KeyPress(key)

  def MouseClick(self, x, y, button):
    self.currentScreen.MouseClick(x, y, button)
  
  def onDraw(self):
    if self.paused:
      self.PauseScreen.onDraw()
    else:
      self.currentScreen.onDraw()

  def update(self, dt):
    if self.paused:
      self.PauseScreen.update(dt)
    else:
      self.currentScreen.update(dt)
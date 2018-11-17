import pyglet
from Actors.Slime import *
from Actors.Player import *

class LevelOne:
  
  def __init__(self, window, screenManager):
    print ("Creating Level One")
    self.window = window
    self.batch = pyglet.graphics.Batch()
    self.screenManager = screenManager
    self.player = Player(self.batch, 320,0)

    self.label = pyglet.text.Label('Level One',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
    
  
  def KeyPress(self, key):
    print("L1 KeyPress")
    if key == 97:
      print("Move Left")
      self.player.MoveLeft()
    elif key == 100:
      print("Move Right")
      self.player.MoveRight()
    if key == 32:
      print ("Jump")
      self.player.Jump()

  def KeyUp(self, key):
    if key == 97:
      print("Stop Move Left")
      self.player.StopMoveLeft()
    elif key == 100:
      print("Stop Move Right")
      self.player.StopMoveRight()

  def MouseClick(self, x, y, button):
    self.screenManager.SetScreen("LevelTwo")
  
  def onDraw(self):
    self.window.clear()
    self.label.draw()
    self.batch.draw()

  def update(self, dt):
    self.player.update(dt)
import pyglet

from AssetManager import *

class Player:

  def __init__(self, batch, x, y):
    self.group = pyglet.graphics.OrderedGroup(3)
    self.batch = batch
    self.Jumping = False
    self.MovingRight = False
    self.MovingLeft = False
    self.x = x
    self.y = y

    self.hSpeed = 10
    self.vSpeed = 10

  def Jump(self):
    print("Jumping")
    if not self.Jumping:
      self.Jumping = True
      self.JumpTime = 0
  
  def MoveLeft(self):
    print("MoveLeft")
    self.MovingLeft = True

  def MoveRight(self):
    print("MoveRight")
    self.MovingRight = True
  
  def StopMoveLeft(self):
    print("MoveLeft")
    self.MovingLeft = False

  def StopMoveRight(self):
    print("MoveRight")
    self.MovingRight = False
  
  def update(self, dt):
    if self.MovingRight:
      self.x += self.hSpeed*dt
      print(self.x)
    if self.MovingLeft:
      print(self.x)
      self.x -= self.hSpeed*dt
    if self.Jumping:
      print(self.y, self.JumpTime)
      self.JumpTime += dt
      if self.JumpTime <= .5:
        self.y += self.vSpeed
      else:
        self.y -= self.vSpeed
      if self.JumpTime >= 1:
        self.Jumping = False
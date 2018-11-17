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

    self.hSpeed = 128
    self.vSpeed = 256

    self.currentAnimation = pyglet.sprite.Sprite(AssetManager.getInstance().playerIdle, batch=self.batch, group=self.group)
    self.SetAnimationLocation()

  def Jump(self):
    print("Jumping")
    if not self.Jumping:
      self.Jumping = True
      self.JumpTime = 0
  
  def SetAnimationLocation(self):
    self.currentAnimation.x = self.x
    self.currentAnimation.y = self.y

  def MoveLeft(self):
    print("MoveLeft")
    self.MovingLeft = True

  def MoveRight(self):
    print("MoveRight")
    self.MovingRight = True
  
  def StopMoveLeft(self):
    print("StopMoveLeft")
    self.MovingLeft = False

  def StopMoveRight(self):
    print("StopMoveRight")
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
      if self.JumpTime <= 1:
        self.y += self.vSpeed*dt
      else:
        self.y -= self.vSpeed*dt
      if self.JumpTime >= 2:
        self.Jumping = False
    self.SetAnimationLocation()
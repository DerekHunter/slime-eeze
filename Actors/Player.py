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
    self.gravity = 4
    self.jumpPower = 45
    self.vSpeed = 0

    self.currentAnimation = pyglet.sprite.Sprite(AssetManager.getInstance().playerIdle, batch=self.batch, group=self.group)
    self.SetAnimationLocation()

  def Jump(self):
    self.vSpeed = self.jumpPower
  
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
  
  def update(self, dt, collidables, cameraOffset):
    print("PLayer: ",self.x,self.y)

    self.y += self.vSpeed
    for collidable in collidables:
      if self.x+64 >= collidable.x-cameraOffset:
        if self.x+64 <= collidable.x+128 -cameraOffset:
          if self.y <= collidable.y+128:
            self.y = collidable.y+128
            self.vSpeed = 0
            break
    self.vSpeed -= self.gravity
    

    self.SetAnimationLocation()
import pyglet

from random import randint
from AssetManager import *

class Slime:

  def __init__(self, batch, x, y):
    print(x,y)
    self.group = pyglet.graphics.OrderedGroup(5)
    self.batch = batch
    self.slimeSinging = AssetManager.getInstance().slimeSinging
    self.slimeHopping = AssetManager.getInstance().slimeHopping
    self.slimeSad = AssetManager.getInstance().slimeSad
    self.slimeThinking = AssetManager.getInstance().slimeThinking
    self.slimeLaughing = AssetManager.getInstance().slimeLaughing
    self.slimeIdle = AssetManager.getInstance().slimeIdle
    self.x = x
    self.y = y
    self.currentAnimation = pyglet.sprite.Sprite(self.slimeIdle, batch=self.batch, group=self.group)
    self.state = "idle"
    self.moveSpeed = 10

    if randint(0,6) == 0:
      self.SetHopping()
    if randint(0,6) == 1:
      self.SetIdle()
    if randint(0,6) == 2:
      self.SetLaughing()
    if randint(0,6) == 3:
      self.SetSad()
    if randint(0,6) == 4:
      self.SetSinging()
    if randint(0,6) == 5:
      self.SetThinking()



  def ToggleAnimation(self):
    if self.state == "singing":
      self.state = "hopping"
      self.SetHopping()
    elif self.state == "hopping":
      self.state = "sad"
      self.SetSad()
    elif self.state == "sad":
      self.state = "thinking"
      self.SetThinking()
    elif self.state == "thinking":
      self.state = "laughing"
      self.SetLaughing()
    elif self.state == "laughing":
      self.state = "idle"
      self.SetIdle()
    elif self.state == "idle":
      self.state = "singing"
      self.SetSinging()

  def SetCurrentAnimation(self, image):
    self.currentAnimation.batch = None
    self.currentAnimation = pyglet.sprite.Sprite(image, batch=self.batch, group=self.group)
    self.currentAnimation.x = self.x
    self.currentAnimation.y = self.y

  def SetHopping(self):
    print("Setting Hopping")
    self.SetCurrentAnimation(self.slimeHopping)

  def SetLaughing(self):
    print("Setting Laughing")
    self.SetCurrentAnimation(self.slimeLaughing)

  def SetIdle(self):
    print("Setting Idle")
    self.SetCurrentAnimation(self.slimeIdle)

  def SetSinging(self):
    print("Setting Singing")
    self.SetCurrentAnimation(self.slimeSinging)
  
  def SetSad(self):
    print("Setting Sad")
    self.SetCurrentAnimation(self.slimeSad)

  def SetThinking(self):
    print("Setting Thinking")
    self.SetCurrentAnimation(self.slimeThinking)

  def MoveTo(self, x, y):
    print("Moving Slime")
    self.SetHopping()

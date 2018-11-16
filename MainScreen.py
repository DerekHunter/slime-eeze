import pyglet

class MainScreen:

  def __init__ (self, window):
    print ("Creating Main Screen ")
    self.window = window
    self.MenuImage = pyglet.image.load("Assets/menu_image.png")
    self.MenuImage.scale = 1.28, 1.2
  
  def KeyPress(self, key):
    pass

  def MouseClick(self, x, y, button):
    pass
  
  def onDraw(self):
    self.window.clear()
    self.MenuImage.blit(0,0)

  def update(self, dt):
    pass
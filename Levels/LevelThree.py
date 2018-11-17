import pyglet


class LevelThree:
  
  def __init__(self, window, screenManager):
    print ("Creating Level One")
    self.window = window
    self.batch = pyglet.graphics.Batch()
    self.screenManager = screenManager
    self.label = pyglet.text.Label('Level Three',
                      font_name='Times New Roman',
                      font_size=36,
                      x=window.width//2, y=window.height-36,
                      anchor_x='center', anchor_y='center')
  
  def KeyPress(self, key):
    pass

  def MouseClick(self, x, y, button):
    self.screenManager.SetScreen("Menu")
  
  def onDraw(self):
    self.window.clear()
    self.label.draw()
    self.batch.draw()

  def update(self, dt):
    pass
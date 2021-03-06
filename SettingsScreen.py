import pyglet

class SettingsScreen:

  def __init__ (self, window, screenManager):
    print ("Creating Settings Screen ")
    self.window = window
    self.batch = pyglet.graphics.Batch()
    self.screenManager = screenManager
    self.label = pyglet.text.Label('Paused',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

  def KeyPress(self, key):
    pass

  def KeyUp(self, key):
    pass

  def MouseClick(self, x, y, button):
    pass

  def onDraw(self):
    self.window.clear()
    self.label.draw()
    self.batch.draw()

  def update(self, dt):
    pass
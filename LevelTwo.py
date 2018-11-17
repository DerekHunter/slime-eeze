import pyglet


class LevelTwo:
  
  def __init__(self, window, screenManager):
    print ("Creating Level Two")
    self.window = window
    self.batch = pyglet.graphics.Batch()
    self.screenManager = screenManager
    self.label = pyglet.text.Label('Level Two',
                      font_name='Times New Roman',
                      font_size=36,
                      x=window.width//2, y=window.height//2,
                      anchor_x='center', anchor_y='center')
  
  def KeyPress(self, key):
    pass

  def MouseClick(self, x, y, button):
    self.screenManager.SetScreen("LevelThree")
  
  def onDraw(self):
    self.window.clear()
    self.label.draw()
    self.batch.draw()

  def update(self, dt):
    pass
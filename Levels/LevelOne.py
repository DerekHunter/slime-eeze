import pyglet
from Actors.Slime import *
from Actors.Player import *
from Tiles.Tile import *
class LevelOne:
  
  def __init__(self, window, screenManager):
    print ("Creating Level One")
    self.window = window
    self.batch = pyglet.graphics.Batch()
    self.screenManager = screenManager
    self.player = Player(self.batch, 128, 128)
    self.cameraOffset = 0
    
    self.hSpeed = 128
    
    self.MoveLeft = False
    self.MoveRight = False

    self.tiles = []
    for i in range(0,10):
      for j in range(0,20):
        if i == 9:
          self.tiles.append(Tile(self.batch, j, i, AssetManager.getInstance().TileNoGrass))
        if i == 8:
          self.tiles.append(Tile(self.batch, j, i, AssetManager.getInstance().TileGrassTop))

    #Tower
    self.tiles.append(Tile(self.batch, 3, 7, AssetManager.getInstance().TileGrassTopLeft))
    self.tiles.append(Tile(self.batch, 4, 7, AssetManager.getInstance().TileGrassRight))
    self.tiles.append(Tile(self.batch, 4, 6, AssetManager.getInstance().TileGrassTop))

    # #Boulder
    # self.levelData[7][12] = 4
    # self.levelData[7][13] = 4
    # self.levelData[6][12] = 4
    # self.levelData[6][13] = 4

    # #Slime
    # self.levelData[7][8] = 2

    # #Hole
    # self.levelData[8][16] = 0
    # self.levelData[8][17] = 0
    # self.levelData[9][16] = 0
    # self.levelData[9][17] = 0
    
    # #Finisher
    # self.levelData[8][19] = 3

    # for row in self.levelData:
    #   print(row)

    self.label = pyglet.text.Label('Level One',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height-36,
                          anchor_x='center', anchor_y='center')

  def KeyPress(self, key):
    print("L1 KeyPress")
    if key == 97:
      print("Move Left")
      self.MoveRight = True
      self.player.MoveLeft()
    elif key == 100:
      print("Move Right")
      self.MoveLeft = True
      self.player.MoveRight()
    if key == 32:
      print ("Jump")
      self.player.Jump()

  def KeyUp(self, key):
    if key == 97:
      print("Stop Move Left")
      self.MoveRight = False
      self.player.StopMoveLeft()
    elif key == 100:
      print("Stop Move Right")
      self.MoveLeft = False
      self.player.StopMoveRight()

  def MouseClick(self, x, y, button):
    self.screenManager.SetScreen("LevelTwo")
  
  def onDraw(self):
    self.window.clear()
    self.label.draw()
    self.batch.draw()

  def update(self, dt):
    if self.MoveLeft:
      self.cameraOffset += self.hSpeed*dt
    if self.MoveRight:
      self.cameraOffset -= self.hSpeed*dt
    if self.cameraOffset > 640:
      self.cameraOffset = 640
    if self.cameraOffset < 0:
      self.cameraOffset = 0
    for tile in self.tiles:
      tile.update(dt, self.cameraOffset)
    self.player.update(dt)
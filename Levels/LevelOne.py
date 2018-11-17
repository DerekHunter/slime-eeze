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
    self.player = Player(self.batch, 128, 300)
    self.cameraOffset = 0
    
    self.hSpeed = 128
    
    self.MoveLeft = False
    self.MoveRight = False
    self.group = pyglet.graphics.OrderedGroup(3)
    self.currentAnimation = pyglet.sprite.Sprite(AssetManager.getInstance().Background, batch=self.batch, group=self.group)

    
    self.tiles = []

    #this one can be the cage if we get it
    self.tiles.append(Tile(self.batch, 10, 7, AssetManager.getInstance().ground5))

    #steps
    self.tiles.append(Tile(self.batch, 14, 6, AssetManager.getInstance().grassleft))
    self.tiles.append(Tile(self.batch, 15, 5, AssetManager.getInstance().grassleft))
    self.tiles.append(Tile(self.batch, 16, 4, AssetManager.getInstance().grassleft))
    self.tiles.append(Tile(self.batch, 17, 4, AssetManager.getInstance().ground0))
    self.tiles.append(Tile(self.batch, 18, 4, AssetManager.getInstance().grassright))
    #tower
    self.tiles.append(Tile(self.batch, 3, 7, AssetManager.getInstance().ground5))
    self.tiles.append(Tile(self.batch, 4, 7, AssetManager.getInstance().ground5))
    self.tiles.append(Tile(self.batch, 4, 6, AssetManager.getInstance().ground5))

    #obstacle wall
    self.tiles.append(Tile(self.batch, 20, 7, AssetManager.getInstance().ground5))
    self.tiles.append(Tile(self.batch, 20, 6, AssetManager.getInstance().ground5))
    self.tiles.append(Tile(self.batch, 20, 5, AssetManager.getInstance().ground5))

    #second steps
    self.tiles.append(Tile(self.batch, 25, 6, AssetManager.getInstance().grassleft))
    self.tiles.append(Tile(self.batch, 26, 5, AssetManager.getInstance().grassleft))
    self.tiles.append(Tile(self.batch, 27, 4, AssetManager.getInstance().grassleft))
    self.tiles.append(Tile(self.batch, 28, 4, AssetManager.getInstance().ground0))
    self.tiles.append(Tile(self.batch, 29, 4, AssetManager.getInstance().grassright))
    #Boulder will be at 29, 3, ontop of the second steps


    # pre first hole
    for i in range(0,10):
      for j in range(0,29):
        if i == 9:
          self.tiles.append(Tile(self.batch, j, i, AssetManager.getInstance().ground5))
        if i == 8:
          self.tiles.append(Tile(self.batch, j, i, AssetManager.getInstance().grass2))
    #between hole and bit
    for i in range(0,10):
      for j in range(31,35):
        if i == 9:
          self.tiles.append(Tile(self.batch, j, i, AssetManager.getInstance().ground5))
        if i == 8:
          self.tiles.append(Tile(self.batch, j, i, AssetManager.getInstance().grass2))
   #post pit
    for i in range(0,10):
      for j in range(40,50):
        if i == 9:
          self.tiles.append(Tile(self.batch, j, i, AssetManager.getInstance().ground5))
        if i == 8:
          self.tiles.append(Tile(self.batch, j, i, AssetManager.getInstance().grass2))


    #Tower
  #  self.tiles.append(Tile(self.batch, 3, 7, AssetManager.getInstance().TileGrassTopLeft))
  #  self.tiles.append(Tile(self.batch, 4, 7, AssetManager.getInstance().TileGrassRight))
  #  self.tiles.append(Tile(self.batch, 4, 6, AssetManager.getInstance().TileGrassTop))

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
      # for tile in self.tiles:
      #   if self.player.y >= tile.y:
      #     if self.player.y <= tile.y+128:
      #       print("Found Collidable", tile.x-self.cameraOffset)
      #       if self.player.x+128 >= tile.x-self.cameraOffset:
      #         print("Collision")
      #         self.player.x = tile.x
      #         break
    if self.MoveRight:
      self.cameraOffset -= self.hSpeed*dt
    if self.cameraOffset > 189273:
      self.cameraOffset = 640
    if self.cameraOffset < 0:
      self.cameraOffset = 0
    
    

    
    for tile in self.tiles:
      tile.update(dt, self.cameraOffset)
    self.player.update(dt, self.tiles, self.cameraOffset)
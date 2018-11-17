import pyglet

class AssetManager:
  __instance = None
  @staticmethod 
  def getInstance():
    """ Static access method. """
    if AssetManager.__instance == None:
        AssetManager()
    return AssetManager.__instance

  def __init__(self):
    """ Virtually private constructor. """
    if AssetManager.__instance != None:
        raise Exception("This class is a singleton!")
    else:
      AssetManager.__instance = self

      ########## Slimes  ###################
      self.__instance.slimeSinging = pyglet.image.load_animation('./Assets/Slime/SlimeSinging.gif')
      self.__instance.slimeHopping = pyglet.image.load_animation('Assets/Slime/Slime.gif')
      self.__instance.slimeSad = pyglet.image.load_animation('Assets/Slime/SlimeSad.gif')
      self.__instance.slimeThinking = pyglet.image.load_animation('Assets/Slime/SlimeThinking.gif')
      self.__instance.slimeLaughing = pyglet.image.load_animation('Assets/Slime/SlimeLaughing.gif')
      self.__instance.slimeIdle = pyglet.image.load_animation('Assets/Slime/SlimeIdle.gif')

      ########## Player ###################
      self.__instance.playerIdle = pyglet.image.load_animation('Assets/Character/CharacterIdle.gif')
      
      ########## Menu ###################
      self.__instance.MenuBackground = pyglet.image.load_animation("Assets/MainMenu/MainMenuBackGround.gif")
      self.__instance.MenuWords = pyglet.resource.image("Assets/MainMenu/MainMenuWords.png")
      self.__instance.MenuStartHighlight = pyglet.resource.image("Assets/MainMenu/MainMenuStartHighlight.png")
      self.__instance.MenuQuitHighlight = pyglet.resource.image("Assets/MainMenu/MainMenuQuitHighlight.png")
      self.__instance.MenuSettingsHighlight = pyglet.resource.image("Assets/MainMenu/MainMenuSettingsHighlight.png")
      

      ########## TILE SET Grass ###################
      self.__instance.TileGrassDown = pyglet.resource.image("Assets/Tileset1/TileGrassDown.png")
      self.__instance.TileGrassDownLeft = pyglet.resource.image("Assets/Tileset1/TileGrassDownLeft.png")
      self.__instance.TileGrassDownRight = pyglet.resource.image("Assets/Tileset1/TileGrassDownRight.png")
      self.__instance.TileGrassLeft = pyglet.resource.image("Assets/Tileset1/TileGrassLeft.png")
      self.__instance.TileGrassRight = pyglet.resource.image("Assets/Tileset1/TileGrassRight.png")
      self.__instance.TileGrassTop = pyglet.resource.image("Assets/Tileset1/TileGrassTop.png")
      self.__instance.TileGrassTopLeft = pyglet.resource.image("Assets/Tileset1/TileGrassTopLeft.png")
      self.__instance.TileGrassTopRight = pyglet.resource.image("Assets/Tileset1/TileGrassTopRight.png")
      self.__instance.TileNoGrass = pyglet.resource.image("Assets/Tileset1/TileNoGrass.png")
      ######### Actual tile set guys##############
      self.__instance.grass1 = pyglet.resource.image("Assets/Tileset3/grass1.png")
      self.__instance.grass2 = pyglet.resource.image("Assets/Tileset3/grass2.png")
      self.__instance.grass3 = pyglet.resource.image("Assets/Tileset3/grass3.png")
      self.__instance.grass4 = pyglet.resource.image("Assets/Tileset3/grass4.png")
      self.__instance.grass5 = pyglet.resource.image("Assets/Tileset3/grass5.png")
      self.__instance.grass6 = pyglet.resource.image("Assets/Tileset3/grass6.png")
      self.__instance.grass7 = pyglet.resource.image("Assets/Tileset3/grass7.png")
      self.__instance.grass8 = pyglet.resource.image("Assets/Tileset3/grass8.png")
      self.__instance.grass9 = pyglet.resource.image("Assets/Tileset3/grass9.png")
      self.__instance.grasscorner1 = pyglet.resource.image("Assets/Tileset3/grasscorner1.png")
      self.__instance.grasscorner2 = pyglet.resource.image("Assets/Tileset3/grasscorner2.png")
      self.__instance.grasscorner3 = pyglet.resource.image("Assets/Tileset3/grasscorner3.png")
      self.__instance.grasscorner4 = pyglet.resource.image("Assets/Tileset3/grasscorner4.png")
      self.__instance.grassleft = pyglet.resource.image("Assets/Tileset3/grassleft.png")
      self.__instance.grassright = pyglet.resource.image("Assets/Tileset3/grassright.png")
      self.__instance.ground5 = pyglet.resource.image("Assets/Tileset3/ground5.png")
      self.__instance.ground0 = pyglet.resource.image("Assets/Tileset3/grasstop/ground0.png")

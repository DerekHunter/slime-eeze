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
      self.__instance.slimeSinging = pyglet.image.load_animation('Assets/Slime/SlimeSinging.gif')
      self.__instance.slimeHopping = pyglet.image.load_animation('Assets/Slime/Slime.gif')
      self.__instance.slimeSad = pyglet.image.load_animation('Assets/Slime/SlimeSad.gif')
      self.__instance.slimeThinking = pyglet.image.load_animation('Assets/Slime/SlimeThinking.gif')
      self.__instance.slimeLaughing = pyglet.image.load_animation('Assets/Slime/SlimeLaughing.gif')
      self.__instance.slimeIdle = pyglet.image.load_animation('Assets/Slime/SlimeIdle.gif')
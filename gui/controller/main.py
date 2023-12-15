from view.window import Window
from .interface import IController


class Controller(IController):
  def __init__(self):
    self.__view = Window(self)

  def main(self):
    self.__view.create_window()

  def load_file(self, filename):
    print(filename)

from view.window import Window


class Controller:
  def __init__(self):
    self.__view = Window()

  def main(self):
    self.__view.create_window()

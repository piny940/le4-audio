from view.window import Window


class Controller:
  def __init__(self):
    self.__view = Window()

  def main(self):
    self.__view.create_window()
    self.__view.spectrogram.draw([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

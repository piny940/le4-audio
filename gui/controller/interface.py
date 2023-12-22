from abc import ABCMeta, abstractmethod


class IController(metaclass=ABCMeta):
  @abstractmethod
  def main(self):
    pass

  @abstractmethod
  def load_file(self, filename):
    pass

  @abstractmethod
  def update_figures(self, waveform):
    pass

  @abstractmethod
  def update_start(self, start):
    pass

  @abstractmethod
  def update_end(self, end):
    pass

  @abstractmethod
  def update_play_button(self):
    pass

  @abstractmethod
  def play(self):
    pass

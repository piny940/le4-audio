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
  def play(self):
    pass
  
  @abstractmethod
  def stop(self):
    pass

  @abstractmethod
  def apply_voice_change(self):
    pass
  
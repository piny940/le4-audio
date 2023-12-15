from abc import ABCMeta, abstractmethod


class IController(metaclass=ABCMeta):
  @abstractmethod
  def main(self):
    pass

  @abstractmethod
  def load_file(self, filename):
    pass

from view.window import Window
from .interface import IController
from core.core import *
from core.constants import SR, SIZE_FRAME, SHIFT_SIZE
import matplotlib.pyplot as plt


class Controller(IController):
  def __init__(self):
    self.__view = Window(self)

  def main(self):
    plt.rcParams.update({'font.size': 6})
    self.__view.create_window()

  def load_file(self, filename):
    waveform = load_waveform(filename)
    spec = spectrogram(waveform, SIZE_FRAME, SHIFT_SIZE)
    self.__view.figures.draw(spec)

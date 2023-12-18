from view.window import Window
from .interface import IController
from core.core import *
from core.constants import SR, SIZE_FRAME, SHIFT_SIZE
import matplotlib.pyplot as plt
from core.wave_range import WaveRange


class Controller(IController):
  def __init__(self):
    self.__view = Window(self)

  def main(self):
    plt.rcParams.update({'font.size': 6})
    self.__view.create_window()
    self.__waveform = None
    self.__wave_range = None

  def load_file(self, filename):
    self.__waveform = load_waveform(filename)
    self.__wave_range = WaveRange(self.__waveform)
    self.update_figures(self.__wave_range.get_waveform())
    self.__view.start_slider.draw(self.__waveform, self.__wave_range.get_start())
    self.__view.end_slider.draw(self.__waveform, self.__wave_range.get_end())

  def update_figures(self, waveform):
    spec = spectrogram(waveform, SIZE_FRAME, SHIFT_SIZE)
    f0s = get_f0s(waveform, SR, SIZE_FRAME)
    self.__view.figures.draw(spec, f0s)

  def update_start(self, start):
    self.__wave_range.set_start(start)
    self.update_figures(self.__wave_range.get_waveform())
    self.__view.start_slider.draw(self.__waveform, self.__wave_range.get_start())

  def update_end(self, end):
    self.__wave_range.set_end(end)
    self.update_figures(self.__wave_range.get_waveform())
    self.__view.end_slider.draw(self.__waveform, self.__wave_range.get_end())

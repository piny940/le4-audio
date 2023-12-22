from view.window import Window
from .interface import IController
from core.core import *
from core.constants import SR, SIZE_FRAME, SHIFT_SIZE
import matplotlib.pyplot as plt
from core.wave_range import WaveRange
from view.audio import AudioPlayer


class Controller(IController):
  def __init__(self):
    self.__view = Window(self)
    self.__spec = None
    self.__f0s = None
    self.__melody = None
    self.__audio_player = AudioPlayer()

  def main(self):
    plt.rcParams.update({'font.size': 6})
    self.__view.create_window()
    self.__waveform = None
    self.__wave_range = None

  def load_file(self, filename):
    self.__waveform = load_waveform(filename)
    self.__wave_range = WaveRange(self.__waveform)
    self.calc()
    self.update_figures(self.__wave_range)
    self.__view.play_button.draw()
    self.__view.stop_button.draw()
    self.__view.start_slider.draw(self.__waveform, self.__wave_range.get_start())
    self.__view.end_slider.draw(self.__waveform, self.__wave_range.get_end() -1)
    self.__view.control_panel.draw()

  def calc(self):
    self.__spec = spectrogram(self.__waveform, SIZE_FRAME, SHIFT_SIZE)
    self.__f0s = get_f0s(self.__waveform, SR, SIZE_FRAME)
    self.__melody = get_melody(self.__spec)

  def update_figures(self, wave_range: WaveRange):
    self.__view.figures.draw(self.__spec, self.__f0s, self.__melody, wave_range)
  
  def update_start(self, start: str):
    self.__wave_range.set_start(int(start))
    self.update_figures(self.__wave_range)
    self.__view.start_slider.set_value(self.__wave_range.get_start())
  
  def update_end(self, end: str):
    self.__wave_range.set_end(int(end))
    self.update_figures(self.__wave_range)
    self.__view.end_slider.set_value(self.__wave_range.get_end() - 1)

  def play(self):
    start = self.__wave_range.get_start()
    end = self.__wave_range.get_end()
    self.__audio_player.set_wave(self.__waveform[start:end])
    self.__audio_player.play()
  
  def stop(self):
    self.__audio_player.stop()
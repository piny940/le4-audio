import simpleaudio as sa
from core.constants import *

class AudioPlayer:
  def __init__(self):
    self.__waveform = None
    self.__wave_obj = None
    self.__play_obj = None
  
  def set_wave(self, waveform):
    self.__waveform = waveform
    self.__wave_obj = sa.WaveObject(
      waveform,
      sample_rate=SR,
      num_channels=1,
      bytes_per_sample=4
    )
  
  def play(self):
    if self.__waveform is None:
      print("No waveform to play")
      return
    if self.__play_obj is not None:
      self.__play_obj.stop()
    self.__play_obj = self.__wave_obj.play()
    
  def stop(self):
    if self.__play_obj is None:
      return
    self.__play_obj.stop()
    self.__play_obj = None

  def is_playing(self) -> bool:
    if self.__play_obj is None:
      return False
    return self.__play_obj.is_playing()
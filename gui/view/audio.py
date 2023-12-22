import simpleaudio as sa
from core.constants import *

class AudioPlayer:
  def __init__(self):
    self.__waveform = None
    self.__wave_obj = None
    self.__play_obj = None
  
  def set_wave(self, waveform):
    self.__waveform = waveform
    self.__wave_obj = sa.WaveObject(waveform, 1, 2, SR)
  
  def play(self):
    if self.__waveform is None:
      print("No waveform to play")
      return
    self.__play_obj = self.__wave_obj.play()
    
  def stop(self):
    self.__play_obj.wait_done()

  def is_playing(self) -> bool:
    if self.__play_obj is None:
      return False
    return self.__play_obj.is_playing()
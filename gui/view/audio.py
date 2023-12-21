import simpleaudio

class AudioPlayer:
  def __init__(self):
    self.__playing = False
    self.__waveform = None
  
  def set_wave(self, waveform):
    self.__waveform = waveform
  
  def play(self):
    if self.__waveform is None:
      print("No waveform to play")
      return
    self.__playing = True
    
class WaveRange:
  def __init__(self, waveform):
    self.__waveform = waveform
    self.__start = 0
    self.__end = len(waveform)

  def get_waveform(self):
    return self.__waveform[self.__start: self.__end]

  def get_start(self):
    return self.__start

  def get_end(self):
    return self.__end

  def set_start(self, start):
    if start > self.__end:
      return
    self.__start = start

  def set_end(self, end):
    if end < self.__start:
      return
    self.__end = end

class WaveRange:
  MIN_SIZE = 2500
  
  def __init__(self, waveform):
    self.__start = 0
    self.__end = len(waveform)

  def get_start(self):
    return self.__start

  def get_end(self):
    return self.__end

  def set_start(self, start: int):
    if start >= self.__end - self.MIN_SIZE:
      return
    self.__start = start

  def set_end(self, end: int):
    if end <= self.__start + self.MIN_SIZE:
      return
    self.__end = end

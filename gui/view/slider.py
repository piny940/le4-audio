from controller.interface import IController
import tkinter as tk
from .view_base import ViewBase

class Slider(ViewBase):
  def __init__(self, frame: tk.Frame, c: IController, command=None):
    self.__command = command
    super().__init__(frame, c)

  def draw(self, from_, to, value=None):
    self.slider = tk.Scale(
        command=self.__command,
        master=self._frame,
        from_=from_,
        to=to,
        label=u'時間[sample]',
        orient=tk.HORIZONTAL,
        length=700,
        width=15,
    )
    self.slider.set(value)
    self.slider.pack()
    self._set([self.slider])

  def get_value(self):
    return self.slider.get()
  def set_value(self, value: int):
    self.slider.set(value)


class StartSlider(Slider):
  def __init__(self, frame: tk.Frame, c: IController):
    super().__init__(frame, c, c.update_start)

  def draw(self, waveform, value=None):
    super().draw(0, len(waveform) - 1, value=value)


class EndSlider(Slider):
  def __init__(self, frame: tk.Frame, c: IController):
    super().__init__(frame, c, c.update_end)

  def draw(self, waveform, value=None):
    super().draw(0, len(waveform) - 1, value=value)

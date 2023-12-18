from controller.interface import IController
import tkinter as tk


class Slider:
  def __init__(self, frame: tk.Frame, c: IController, command=None):
    self.__frame = frame
    self.__c = c
    self.__command = command

  def draw(self, from_, to, value=None):
    slider = tk.Scale(
        value=value,
        command=self.__command,
        master=self.__frame,
        from_=from_,
        to=to,
        label=u'時間[sample]',
        orient=tk.HORIZONTAL,
        length=700,
        width=30,
    )
    slider.pack()


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

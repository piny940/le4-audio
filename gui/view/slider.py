from controller.interface import IController
import tkinter as tk


class Slider:
  def __init__(self, frame: tk.Frame, c: IController):
    self.__frame = frame
    self.__c = c

  def draw(self, from_, to):
    slider = tk.Scale(
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
    super().__init__(frame, c)

  def draw(self, waveform):
    super().draw(0, len(waveform) - 1)


class EndSlider(Slider):
  def __init__(self, frame: tk.Frame, c: IController):
    super().__init__(frame, c)

  def draw(self, waveform):
    super().draw(0, len(waveform) - 1)

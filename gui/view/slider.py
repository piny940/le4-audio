from controller.interface import IController
import tkinter as tk


class Slider:
  def __init__(self, frame: tk.Frame, c: IController, command=None):
    self.__frame = frame
    self.__c = c
    self.__command = command
    self.__slider = None

  def draw(self, from_, to, value=None):
    if self.__slider is not None:
      self.__slider.destroy()
    self.__slider = tk.Scale(
        command=self.__command,
        master=self.__frame,
        from_=from_,
        to=to,
        label=u'時間[sample]',
        orient=tk.HORIZONTAL,
        length=700,
        width=30,
    )
    self.__slider.set(value)
    self.__slider.pack()

  def get_value(self):
    return self.__slider.get()
  def set_value(self, value: int):
    self.__slider.set(value)


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

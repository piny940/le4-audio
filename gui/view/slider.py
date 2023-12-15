from controller.interface import IController
import tkinter as tk


class Slider:
  def __init__(self, frame, c: IController):
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
        width=40,
    )
    slider.pack()

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from core.constants import SR


class Figures:
  def __init__(self, frame: tk.Frame):
    self.__frame = frame
    self.__fig = plt.figure(figsize=(3, 2))
    self.__spec_ax = None
    self.__f0s_ax = None
    canvas = FigureCanvasTkAgg(self.__fig, master=self.__frame)
    canvas.get_tk_widget().pack(side='left')

  def draw(self, spectrogram, f0s):
    self.draw_spectrogram(spectrogram)
    self.draw_f0s(f0s)
    self.__fig.tight_layout()
    self.__fig.canvas.draw()

  def draw_spectrogram(self, spectrogram):
    if self.__spec_ax is not None:
      self.__fig.delaxes(self.__spec_ax)
    self.__spec_ax = self.__fig.add_subplot(1, 2, 1)
    Spectrogram(self.__spec_ax).draw(spectrogram)

  def draw_f0s(self, f0s):
    if self.__f0s_ax is not None:
      self.__fig.delaxes(self.__f0s_ax)
    self.__f0s_ax = self.__fig.add_subplot(1, 2, 2)
    F0s(self.__f0s_ax).draw(f0s)


class Spectrogram:
  def __init__(self, ax: Axes):
    self.__ax = ax
    self.__ax.set_xlabel('sec')
    self.__ax.set_ylabel('frequency [Hz]')

  def draw(self, spectrogram):
    self.__ax.imshow(
        np.flipud(np.array(spectrogram).T),
        extent=[0, len(spectrogram), 0, SR / 2],
        aspect='auto',
        interpolation='nearest'
    )


class F0s:
  def __init__(self, ax: Axes):
    self.__ax = ax
    self.__ax.set_xlabel('sec')
    self.__ax.set_ylabel('frequency [Hz]')

  def draw(self, f0s):
    self.__ax.plot(f0s)

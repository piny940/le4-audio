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
    canvas = FigureCanvasTkAgg(self.__fig, master=self.__frame)
    canvas.get_tk_widget().pack(side='left')

  def draw(self, spectrogram):
    for ax in self.__fig.axes:
      self.__fig.delaxes(ax)
    ax1 = self.__fig.add_subplot(1, 2, 1)
    Spectrogram(ax1).draw(spectrogram)

    ax2 = self.__fig.add_subplot(1, 2, 2)
    ax2.tick_params()
    ax2.imshow(
        np.flipud(np.array(spectrogram).T),
        extent=[0, len(spectrogram), 0, SR / 2],
        aspect='auto',
        interpolation='nearest'
    )
    self.__fig.tight_layout()
    self.__fig.canvas.draw()


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

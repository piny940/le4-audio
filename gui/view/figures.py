import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from core.constants import SR, SHIFT_SIZE
from core.wave_range import WaveRange

class Figures:
  def __init__(self, frame: tk.Frame):
    self.__frame = frame
    self.__fig = plt.figure(figsize=(5, 2))
    self.__spec_ax = None
    self.__melody_ax = None
    canvas = FigureCanvasTkAgg(self.__fig, master=self.__frame)
    canvas.get_tk_widget().pack(side='left')

  def draw(self, spectrogram, f0s, melody, wave_range: WaveRange):
    for ax in self.__fig.axes:
      self.__fig.delaxes(ax)
    self.__spec_ax = self.__fig.add_subplot(121)
    SpecWithF0s(self.__spec_ax).draw(spectrogram, f0s, wave_range)
    self.__melody_ax = self.__fig.add_subplot(122)
    Melody(self.__melody_ax).draw(melody, wave_range)
    self.__fig.tight_layout()
    self.__fig.canvas.draw()


class SpecWithF0s:
  def __init__(self, ax: Axes):
    self.__ax = ax
    self.__ax.set_xlabel('sample')
    self.__ax.set_ylabel('frequency [Hz]')

  def draw(self, spectrogram, f0s, wave_range: WaveRange):
    self.__ax.imshow(
        np.flipud(np.array(spectrogram).T),
        extent=[0, len(spectrogram), 0, SR / 2],
        aspect='auto',
        interpolation='nearest',
    )
    x_data = np.linspace(0, len(spectrogram), len(f0s))
    self.__ax.plot(x_data, f0s)
    self.__ax.set_xlim(wave_range.get_start() // SHIFT_SIZE, min(wave_range.get_end() // SHIFT_SIZE, len(spectrogram)))
    self.__ax.set_ylim(0, 3000)

class Melody:
  def __init__(self, ax: Axes):
    self.__ax = ax
    self.__ax.set_xlabel('sample')
    self.__ax.set_ylabel('melody')

  def draw(self, melody, wave_range: WaveRange):
    self.__ax.plot(melody)
    self.__ax.set_xlim(wave_range.get_start() // SHIFT_SIZE, min(wave_range.get_end() // SHIFT_SIZE, len(melody)))


# class Spectrogram:
#   def __init__(self, ax: Axes):
#     self.__ax = ax
#     self.__ax.set_xlabel('sec')
#     self.__ax.set_ylabel('frequency [Hz]')

#   def draw(self, spectrogram):
#     self.__ax.imshow(
#         np.flipud(np.array(spectrogram).T),
#         extent=[0, len(spectrogram), 0, SR / 2],
#         aspect='auto',
#         interpolation='nearest'
#     )


# class F0s:
#   def __init__(self, ax: Axes):
#     self.__ax = ax
#     self.__ax.set_xlabel('sec')
#     self.__ax.set_ylabel('frequency [Hz]')

#   def draw(self, f0s):
#     self.__ax.plot(f0s)

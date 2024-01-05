import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from core.constants import SR, SHIFT_SIZE, NOTES
from core.wave_range import WaveRange
import matplotlib.animation as animation

class Figures:
  def __init__(self, frame: tk.Frame):
    self.__frame = frame
    self.__fig = plt.figure(figsize=(10, 4))
    self.__spec_ax = None
    self.__melody_ax = None
    self.__spec_fig = None
    self.__melody_fig = None
    canvas = FigureCanvasTkAgg(self.__fig, master=self.__frame)
    canvas.get_tk_widget().pack(side=tk.LEFT)

  def draw(self, spectrogram, f0s, melody, wave_range: WaveRange):
    for ax in self.__fig.axes:
      self.__fig.delaxes(ax)
    self.__spec_ax = self.__fig.add_subplot(121)
    self.__spec_fig = SpecWithF0s(self.__spec_ax)
    self.__spec_fig.draw(spectrogram, f0s, wave_range)
    self.__melody_ax = self.__fig.add_subplot(122)
    self.__melody_fig = Melody(self.__melody_ax)
    self.__melody_fig.draw(melody, wave_range)
    animation.FuncAnimation(
      self.__fig,
      self.animate,
      interval=1000,
      blit=True,
      save_count=50
    )
    self.__fig.tight_layout()
    self.__fig.canvas.draw()
  
  def animate(self, frame_index):
    return self.__spec_fig.animate()

class SpecWithF0s:
  def __init__(self, ax: Axes):
    self.__ax = ax
    self.__ax.set_xlabel('sample')
    self.__ax.set_ylabel('frequency [Hz]')
    self.__spec_im = None
    self.__spec = None
    self.__f0s = None
    self.__xdata = None

  def draw(self, spectrogram, f0s, wave_range: WaveRange):
    self.__spec = np.flipud(np.array(spectrogram).T)
    self.__f0s = f0s
    self.__spec_im = self.__ax.imshow(
        self.__spec,
        extent=[0, len(spectrogram), 0, SR / 2],
        aspect='auto',
        interpolation='nearest',
    )
    self.__xdata = np.linspace(0, len(spectrogram), len(f0s))
    self.__f0s_im, = self.__ax.plot(self.__xdata, f0s)
    self.__ax.set_xlim(wave_range.get_start() // SHIFT_SIZE, min(wave_range.get_end() // SHIFT_SIZE, len(spectrogram)))
    self.__ax.set_ylim(0, 3000)
  
  def animate(self):
    self.__spec_im.set_array(self.__spec)
    self.__f0s_im.set_data(self.__xdata, self.__f0s)
    return self.__f0s_im, self.__spec_im
    # return self.__f0s_im

class Melody:
  def __init__(self, ax: Axes):
    self.__ax = ax
    self.__ax.set_xlabel('sample')
    self.__ax.set_ylabel('melody')

  def draw(self, melody, wave_range: WaveRange):
    self.__ax.plot(list(map(lambda x: x - NOTES[0], melody)))
    plt.yticks(np.arange(24),
           #  list(["A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4",
           #        "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5",
           #        "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5"])
           list(["C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3",
                 "G#3", "A3", "A#3", "B3", "C4", "C#4", "D4", "D#4",
                 "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4"])
           )

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

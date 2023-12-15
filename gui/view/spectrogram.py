import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from core.constants import SR


class Figures:
  def __init__(self, frame: tk.Frame):
    self.__frame = frame

  def draw(self, spectrogram):
    fig = plt.figure(figsize=(4, 2))
    canvas = FigureCanvasTkAgg(fig, master=self.__frame)
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.tick_params(labelsize=7)
    ax1.set_xlabel('sec', fontsize=7)
    ax1.set_ylabel('frequency [Hz]', fontsize=7)
    ax1.imshow(
        np.flipud(np.array(spectrogram).T),
        extent=[0, len(spectrogram), 0, SR / 2],
        aspect='auto',
        interpolation='nearest'
    )

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.tick_params(labelsize=7)
    ax2.imshow(
        np.flipud(np.array(spectrogram).T),
        extent=[0, len(spectrogram), 0, SR / 2],
        aspect='auto',
        interpolation='nearest'
    )
    fig.tight_layout()
    canvas.get_tk_widget().pack(side='left')

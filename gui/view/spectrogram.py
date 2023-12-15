import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from ..core.constants import SR


class Spectrogram:
  def __init__(self, frame):
    self.__frame = frame

  def draw(self, spectrogram):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=self.__frame)
    plt.xlabel('sec')
    plt.ylabel('frequency [Hz]')
    plt.imshow(
        np.flipud(np.array(spectrogram).T),
        extent=[0, len(spectrogram), 0, SR / 2],
        aspect='auto',
        interpolation='nearest'
    )
    canvas.get_tk_widget().pack(side='left')

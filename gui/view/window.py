import tkinter as tk
from .spectrogram import Spectrogram
from .title import Title


class Window:
  def __init__(self):
    # Window
    self.__WindowWidth = 1000
    self.__WindowHeight = 700

    self.spectrogram = None

  def create_window(self):
    # ----- Window & Canvas config -----
    self.__window = tk.Tk()
    self.__window.title("Audio")
    self.__window.geometry(f"{self.__WindowWidth}x{self.__WindowHeight}")

    # ---- Title -----
    title_frame = self.__new_frame()
    self.title = Title(title_frame)
    self.title.draw()

    # spec_frame = self.__new_frame()
    # self.spectrogram = Spectrogram(spec_frame)
    # self.spectrogram.draw([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    self.__window.mainloop()

  def __new_frame(self):
    frame = tk.Frame(self.__window)
    frame.pack(side='left')
    return frame

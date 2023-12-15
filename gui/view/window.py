import tkinter as tk
from .spectrogram import Figures
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
    title_frame = tk.Frame(self.__window, width=1000, height=100)
    title_frame.pack(side=tk.TOP)
    self.title = Title(title_frame)
    self.title.draw()

    spec_frame = tk.Frame(self.__window, width=800, height=400)
    spec_frame.pack(side=tk.TOP)
    self.spectrogram = Figures(spec_frame)
    self.spectrogram.draw([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    self.__window.mainloop()

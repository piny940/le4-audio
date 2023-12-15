import tkinter as tk
from .spectrogram import Spectrogram


class Window:
  def __init__(self):
    # Window
    self.__WindowWidth = 1000
    self.__WindowHeight = 700

    # Title
    self.__TitleCoord = (170, 50)
    self.__TitleSize = 50
    self.__TitleFont = 'Times'

    self.spectrogram = None

  def create_window(self):
    # ----- Window & Canvas config -----
    self.__window = tk.Tk()
    self.__window.title("Audio")
    self.__window.geometry(f"{self.__WindowWidth}x{self.__WindowHeight}")

    # self.__canvas = tk.Canvas(self.__window, width=self.__WindowWidth,
    #                           height=self.__WindowHeight)

    # self.__canvas.grid(row=0, column=0)

    # # ---- Title -----
    # self.__canvas.create_text(
    #     self.__TitleCoord[0],
    #     self.__TitleCoord[1],
    #     text='Audio',
    #     font=(self.__TitleFont, self.__TitleSize),
    #     anchor='nw')

    spec_frame = self.__new_frame()
    self.spectrogram = Spectrogram(spec_frame)
    self.spectrogram.draw([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    self.__window.mainloop()

  def __new_frame(self):
    frame = tk.Frame(self.__window)
    frame.pack(side='left')
    return frame

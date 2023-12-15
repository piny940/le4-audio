import tkinter as tk


class Window:
  def __init__(self):
    # Window
    self.__WindowWidth = 1000
    self.__WindowHeight = 700

    # Title
    self.__TitleCoord = (170, 50)
    self.__TitleSize = 50
    self.__TitleFont = 'Times'

  def create_window(self):
    # ----- Window & Canvas config -----
    self.__window = tk.Tk()
    self.__window.title("Audio")
    self.__window.geometry(f"{self.__WindowWidth}x{self.__WindowHeight}")

    self.__canvas = tk.Canvas(self.__window, width=self.__WindowWidth,
                              height=self.__WindowHeight)

    self.__canvas.grid(row=0, column=0)

    # ---- Title -----
    self.__canvas.create_text(
        self.__TitleCoord[0],
        self.__TitleCoord[1],
        text='Audio',
        font=(self.__TitleFont, self.__TitleSize),
        anchor='nw')

    self.__window.mainloop()

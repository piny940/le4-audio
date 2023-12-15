import tkinter as tk


class CanvasCoord(Coord):
  '''
  CanvasCoord class is 2 dimention vector to express positions in the canvas.
  '''

  def __add__(self, other):
    value = super().__add__(other)
    value.__class__ = CanvasCoord
    return value

  def __sub__(self, other):
    value = super().__sub__(other)
    value.__class__ = CanvasCoord
    return value


class Window:
  def __init__(self):
    # Window
    self.__WindowWidth = 510
    self.__WindowHeight = 700

    # Title
    self.__TitleCoord = CanvasCoord(170, 50)
    self.__TitleSize = 50
    self.__TitleFont = 'Times'

  def create_window(self):
    '''
      This function is supposed to be called when launching a game.
      '''
    # ----- Window & Canvas config -----
    self.__window = tk.Tk()
    self.__window.title("Reversi")
    self.__window.geometry(f"{self.__WindowWidth}x{self.__WindowHeight}")

    self.__canvas = tk.Canvas(self.__window, width=self.__WindowWidth,
                              height=self.__WindowHeight)

    self.__canvas.grid(row=0, column=0)

    # ---- Title -----
    self.__canvas.create_text(
        self.__TitleCoord.x,
        self.__TitleCoord.y,
        text='Reversi',
        font=(self.__TitleFont, self.__TitleSize),
        anchor='nw')

    self.__window.mainloop()

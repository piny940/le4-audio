import tkinter as tk


class Title:
  TITLE_COORD = (170, 50)
  TITLE_SIZE = 50
  TITLE_FONT = 'Times'

  def __init__(self, frame: tk.Frame):
    self.__frame = frame

  def draw(self):
    canvas = tk.Canvas(self.__frame, width=1000, height=700)
    canvas.create_text(
        Title.TITLE_COORD[0],
        Title.TITLE_COORD[1],
        text='Audio',
        font=(Title.TITLE_FONT, Title.TITLE_SIZE),
        anchor='nw')
    canvas.pack()

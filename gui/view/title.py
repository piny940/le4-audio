import tkinter as tk
from .view_base import ViewBase

class Title(ViewBase):
  TITLE_COORD = (50, 50)
  TITLE_SIZE = 50
  TITLE_FONT = 'Times'

  def draw(self):
    canvas = tk.Canvas(self._frame, width=1000, height=100)
    canvas.create_text(
        Title.TITLE_COORD[0],
        Title.TITLE_COORD[1],
        text='Audio',
        font=(Title.TITLE_FONT, Title.TITLE_SIZE),
        anchor='nw')
    canvas.pack()
    self._set([canvas])

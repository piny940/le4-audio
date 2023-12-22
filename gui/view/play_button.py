import tkinter as tk
from .view_base import ViewBase

class PlayButton(ViewBase):
  def draw(self):
    self.button = tk.Button(
      master=self._frame,
      text="Play",
      command=self._c.play
    )
    self.button.pack(side=tk.LEFT)
    self._set([self.button])
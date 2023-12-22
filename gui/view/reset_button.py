import tkinter as tk
from .view_base import ViewBase

class ResetButton(ViewBase):
  def draw(self):
    self.button = tk.Button(
      master=self._frame,
      text="Reset",
      command=self._c.reset
    )
    self.button.pack(side=tk.LEFT)
    self._set([self.button])
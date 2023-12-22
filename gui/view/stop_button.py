import tkinter as tk
from controller.interface import IController
from .view_base import ViewBase

class StopButton(ViewBase):
  def draw(self):
    self.button = tk.Button(
      master=self._frame,
      text="Stop",
      command=self._c.stop
    )
    self.button.pack(side=tk.LEFT)
    self._set([self.button])
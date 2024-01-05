import tkinter as tk
from .view_base import ViewBase

class RealTimeSwitch(ViewBase):
  def draw(self, is_on):
    self.button = tk.Button(
      master=self._frame,
      text="On" if is_on else "Off",
      command=self._c.toggle_real_time
    )
    self.button.pack(side=tk.LEFT)
    self._set([self.button])

import tkinter as tk
from .view_base import ViewBase
from .batch_panel import BatchPanel

class MainPanel(ViewBase):
  def draw(self, is_real_time_on: bool):
    if not is_real_time_on:
      self.batch_panel = BatchPanel(self._frame, self._c)
      self.batch_panel.draw()
      self._set([self.batch_panel])

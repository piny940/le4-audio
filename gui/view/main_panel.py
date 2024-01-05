import tkinter as tk
from .view_base import ViewBase
from .batch_panel import BatchPanel

class MainPanel(ViewBase):
  def draw(self, is_real_time_on: bool):
    self.batch_panel = BatchPanel(self._frame, self._c)
    self.batch_panel.draw()
    self._set([self.batch_panel])

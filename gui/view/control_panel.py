import tkinter as tk
from controller.interface import IController
from .voice_change_panel import VoiceChangePanel
from .view_base import ViewBase

class ControlPanel(ViewBase):
  def draw(self):
    vc_frame = tk.Frame(
      self._frame,
      width=400,
      height=100,
      padx=10,
      pady=10,
      highlightbackground="white",
      highlightthickness=1
    )
    self.voice_change = VoiceChangePanel(vc_frame, self._c)
    vc_frame.pack(side=tk.LEFT)
    self.voice_change.draw()
    self._set([vc_frame])

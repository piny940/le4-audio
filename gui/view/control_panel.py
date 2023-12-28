import tkinter as tk
from .voice_change_panel import VoiceChangePanel
from .view_base import ViewBase
from .tremolo_panel import TremoloPanel
from .vibrato_panel import VibratoPanel

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
    tremolo_frame = tk.Frame(
      self._frame,
      width=400,
      height=100,
      padx=10,
      pady=10,
      highlightbackground="white",
      highlightthickness=1
    )
    self.tremolo = TremoloPanel(tremolo_frame, self._c)
    vibrato_frame = tk.Frame(
      self._frame,
      width=400,
      height=100,
      padx=10,
      pady=10,
      highlightbackground="white",
      highlightthickness=1
    )
    self.vibrato = VibratoPanel(vibrato_frame, self._c)
    vc_frame.pack(side=tk.LEFT)
    tremolo_frame.pack(side=tk.LEFT)
    vibrato_frame.pack(side=tk.LEFT)
    self.voice_change.draw()
    self.tremolo.draw()
    self.vibrato.draw()
    self._set([vc_frame, tremolo_frame, vibrato_frame])

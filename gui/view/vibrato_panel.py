from .view_base import ViewBase
import tkinter as tk
from .text_box import TextBox

class VibratoPanel(ViewBase):
  def draw(self):
    title = tk.Label(
      master=self._frame,
      text="Vibrato",
      font=("Helvetica", 20)
    )
    text_boxes_frame = tk.Frame(
      self._frame,
      width=1200,
      height=100,
      padx=10,
      pady=10
    )
    freq_frame = tk.Frame(
      text_boxes_frame,
      width=400,
      height=100,
      padx=10,
    )
    self.frequency_box = TextBox(freq_frame, self._c)
    depth_frame = tk.Frame(
      text_boxes_frame,
      width=400,
      height=100,
      padx=10,
    )
    self.depth_box = TextBox(depth_frame, self._c)
    tau_frame = tk.Frame(
      text_boxes_frame,
      width=400,
      height=100,
      padx=10,
    )
    self.tau_box = TextBox(tau_frame, self._c)
    freq_frame.pack(side=tk.LEFT)
    depth_frame.pack(side=tk.LEFT)
    tau_frame.pack(side=tk.LEFT)
    apply_button = tk.Button(
      master=self._frame,
      text="Apply",
      command=self._c.apply_vibrato
    )
    title.pack(side=tk.TOP)
    text_boxes_frame.pack(side=tk.TOP)
    apply_button.pack(side=tk.TOP)
    self.frequency_box.draw("Frequency", 10)
    self.depth_box.draw("Depth", 10)
    self.tau_box.draw("Tau", 10)
    self._set([title, self.frequency_box, self.depth_box, self.tau_box, apply_button])

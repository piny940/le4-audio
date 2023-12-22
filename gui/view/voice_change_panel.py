import tkinter as tk
from controller.interface import IController
from .text_box import TextBox
from .view_base import ViewBase

class VoiceChangePanel(ViewBase):
  def draw(self):
    title = tk.Label(
      master=self._frame,
      text="Voice Change",
      font=("Helvetica", 20)
    )
    text_boxes_frame = tk.Frame(
      self._frame,
      width=400,
      height=100,
      padx=10,
      pady=10
    )
    frequency_box = TextBox(text_boxes_frame, self._c)
    apply_button = tk.Button(
      master=self._frame,
      text="Apply",
      command=None # TODO
    )
    title.pack(side=tk.TOP)
    text_boxes_frame.pack(side=tk.TOP)
    apply_button.pack(side=tk.TOP)
    frequency_box.draw("Frequency", 10)
    self._set([title, frequency_box, apply_button])
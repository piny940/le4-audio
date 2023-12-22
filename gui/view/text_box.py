import tkinter as tk
from .view_base import ViewBase

class TextBox(ViewBase):
  def draw(self, label_str: str, width: int):
    self.__text_box = tk.Entry(
      master=self._frame,
      width=width,
    )
    label = tk.Label(
      master=self._frame,
      text=label_str,
    )
    label.pack()
    self.__text_box.pack()
    self._set([label, self.__text_box])
  
  def get_value(self):
    return self.__text_box.get()

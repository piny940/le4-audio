import tkinter as tk
from controller.interface import IController
from typing import Union

class ViewBase():
  def __init__(self, frame: tk.Frame, c: IController):
    self._frame = frame
    self._c = c
    self._widgets: list[tk.Widget] = []

  def _set(self, widgets: Union['list[tk.Widget]', 'list[ViewBase]']):
    for widget in self._widgets:
      widget.destroy()
    self._widgets = widgets

  def destroy(self):
    for widget in self._widgets:
      widget.destroy()
    self._widgets = []

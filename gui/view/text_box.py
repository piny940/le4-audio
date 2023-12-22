import tkinter as tk
from controller.interface import IController

class TextBox:
  def __init__(self, frame: tk.Frame, c: IController):
    self.__frame = frame
    self.__c = c
    self.__text_box = None
  
  def draw(self, label: str, width: int):
    if self.__text_box is not None:
      self.__text_box.destroy()
    self.__text_box = tk.Entry(
      master=self.__frame,
      width=width,
    )
    self.__text_box.pack()
  
  def get_value(self):
    return self.__text_box.get()

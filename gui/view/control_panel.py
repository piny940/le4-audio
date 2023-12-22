import tkinter as tk
from controller.interface import IController
from .text_box import TextBox

class ControlPanel:
  def __init__(self, frame: tk.Frame, c: IController):
    self.__frame = frame
    self.__c = c
    self.__voice_change = TextBox(self.__frame, self.__c)
    self.__voice_change_frame = tk.Frame(self.__frame, width=400, height=100)
    self.__voice_change_frame.pack(side=tk.RIGHT)
  
  def draw(self):
    self.__voice_change.draw("Voice Change", 10)
  
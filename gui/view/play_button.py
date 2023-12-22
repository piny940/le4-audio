import tkinter as tk
from controller.interface import IController

class PlayButton:
  def __init__(self, frame: tk.Frame, c: IController):
    self.__frame = frame
    self.__c = c
    self.__button = None
  
  def draw(self):
    if self.__button is not None:
      self.__button.destroy()
    self.__button = tk.Button(
      master=self.__frame,
      text="Play",
      command=self.__c.play
    )
    self.__button.pack(side=tk.LEFT)
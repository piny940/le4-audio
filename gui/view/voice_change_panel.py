import tkinter as tk
from controller.interface import IController
from .text_box import TextBox

class VoiceChangePanel:
  def __init__(self, frame: tk.Frame, c: IController):
    self.__frame = frame
    self.__c = c
  
  def draw(self):
    self.__title = tk.Label(
      master=self.__frame,
      text="Voice Change",
      font=("Helvetica", 20)
    )
    self.__text_boxes_frame = tk.Frame(
      self.__frame,
      width=400,
      height=100,
      padx=10,
      pady=10
    )
    self.__frequency_box = TextBox(self.__text_boxes_frame, self.__c)
    self.__apply_button = tk.Button(
      master=self.__frame,
      text="Apply",
      command=None # TODO
    )
    self.__title.pack(side=tk.TOP)
    self.__text_boxes_frame.pack(side=tk.TOP)
    self.__apply_button.pack(side=tk.TOP)
    self.__frequency_box.draw("Frequency", 10)
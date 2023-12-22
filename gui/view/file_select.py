import tkinter as tk
from controller.interface import IController


class FileSelect:
  def __init__(self, frame: tk.Frame, c: IController):
    self.__frame = frame
    self.__c = c

  def draw(self):
    button = tk.Button(self.__frame, text='ファイルを選択', command=self.__button_clicked)
    button.pack(side=tk.LEFT)

  def __button_clicked(self):
    filename = tk.filedialog.askopenfilename()
    self.__c.load_file(filename)

import tkinter as tk
from .view_base import ViewBase

class FileSelect(ViewBase):
  def draw(self):
    self.button = tk.Button(self._frame, text='ファイルを選択', command=self.__button_clicked)
    self.button.pack(side=tk.LEFT)
    self._set([self.button])

  def __button_clicked(self):
    filename = tk.filedialog.askopenfilename()
    self._c.load_file(filename)

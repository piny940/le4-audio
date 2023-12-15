import tkinter as tk
from .figures import Figures
from .title import Title
from .file_select import FileSelect
from controller.interface import IController
from .slider import StartSlider, EndSlider


class Window:
  def __init__(self, c: IController):
    # Window
    self.__WindowWidth = 1000
    self.__WindowHeight = 700

    self.__c = c

  def create_window(self):
    # ----- Window & Canvas config -----
    self.__window = tk.Tk()
    self.__window.title("Audio")
    self.__window.geometry(f"{self.__WindowWidth}x{self.__WindowHeight}")

    # ---- Title -----
    title_frame = tk.Frame(self.__window, width=1000, height=100)
    title_frame.pack(side=tk.TOP)
    self.title = Title(title_frame)
    self.title.draw()

    # ----Figures ----
    spec_frame = tk.Frame(self.__window, width=800, height=400)
    spec_frame.pack(side=tk.TOP)
    self.figures = Figures(spec_frame)

    # ---- File Select ----
    file_select_frame = tk.Frame(self.__window, width=1000, height=100)
    file_select_frame.pack(side=tk.TOP)
    self.file_select = FileSelect(file_select_frame, self.__c)
    self.file_select.draw()

    # ---- Start Slider ----
    start_slider_frame = tk.Frame(self.__window, width=1000, height=100)
    start_slider_frame.pack(side=tk.TOP)
    self.start_slider = StartSlider(start_slider_frame, self.__c)

    # ---- End Slider ----
    end_slider_frame = tk.Frame(self.__window, width=1000, height=100)
    end_slider_frame.pack(side=tk.TOP)
    self.end_slider = EndSlider(end_slider_frame, self.__c)

    self.__window.mainloop()

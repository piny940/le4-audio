import tkinter as tk
from .figures import Figures
from .title import Title
from .file_select import FileSelect
from controller.interface import IController
from .slider import StartSlider, EndSlider
from .text_box import TextBox

class Window:
  def __init__(self, c: IController):
    # Window
    self.__WindowWidth = 1300
    self.__WindowHeight = 1080

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
    start_slider_frame = tk.Frame(self.__window, width=1000, height=50)
    start_slider_frame.pack(side=tk.TOP)
    self.start_slider = StartSlider(start_slider_frame, self.__c)

    # ---- End Slider ----
    end_slider_frame = tk.Frame(self.__window, width=1000, height=50)
    end_slider_frame.pack(side=tk.TOP)
    self.end_slider = EndSlider(end_slider_frame, self.__c)

    # ---- Voice Change ----
    voice_change_frame = tk.Frame(self.__window, width=400, height=100)
    voice_change_frame.pack(side=tk.TOP)
    self.voice_change = TextBox(voice_change_frame, self.__c)
    self.voice_change.draw("Voice Change", 10)

    self.__window.mainloop()

import tkinter as tk
from .figures import Figures
from .title import Title
from .file_select import FileSelect
from controller.interface import IController
from .slider import StartSlider, EndSlider
from .text_box import TextBox
from .control_panel import ControlPanel
from .play_button import PlayButton
from .stop_button import StopButton
from .reset_button import ResetButton

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
    self.title = Title(title_frame, self.__c)
    self.title.draw()

    # ----Figures ----
    spec_frame = tk.Frame(self.__window, width=800, height=400)
    spec_frame.pack(side=tk.TOP)
    self.figures = Figures(spec_frame)

    # ---- File Select ----
    middle_buttons_frame = tk.Frame(self.__window, width=1000, height=100)
    middle_buttons_frame.pack(side=tk.TOP)
    self.file_select = FileSelect(middle_buttons_frame, self.__c)
    self.file_select.draw()
    # ---- Play Button ----
    self.play_button = PlayButton(middle_buttons_frame, self.__c)
    self.stop_button = StopButton(middle_buttons_frame, self.__c)
    # ---- Reset Button ----
    self.reset_button = ResetButton(middle_buttons_frame, self.__c)

    # ---- Start Slider ----
    start_slider_frame = tk.Frame(self.__window, width=1000, height=50)
    start_slider_frame.pack(side=tk.TOP)
    self.start_slider = StartSlider(start_slider_frame, self.__c)

    # ---- End Slider ----
    end_slider_frame = tk.Frame(self.__window, width=1000, height=50)
    end_slider_frame.pack(side=tk.TOP)
    self.end_slider = EndSlider(end_slider_frame, self.__c)

    # ---- Control Panel ----
    control_panel_frame = tk.Frame(
      self.__window,
      width=self.__WindowWidth,
      height=380,
      padx=10,
      pady=10
    )
    control_panel_frame.pack(side=tk.TOP)
    self.control_panel = ControlPanel(control_panel_frame, self.__c)

    self.__window.mainloop()

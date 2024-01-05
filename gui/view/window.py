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
from .real_time_switch import RealTimeSwitch
from .batch_panel import BatchPanel
from .main_panel import MainPanel
from core.constants import DEFAULT_REAL_TIME_ON

class Window:
  def __init__(self, c: IController):
    # Window
    self.__WindowWidth = 1300
    self.__WindowHeight = 1080

    self.__c = c

  async def create_window(self):
    # ----- Window & Canvas config -----
    self.__window = tk.Tk()
    self.__window.title("Audio")
    self.__window.geometry(f"{self.__WindowWidth}x{self.__WindowHeight}")

    # ---- Title -----
    title_frame = tk.Frame(self.__window, width=1000, height=100)
    title_frame.pack(side=tk.TOP)
    self.title = Title(title_frame, self.__c)
    self.title.draw()

    # ---- Real Time Switch ----
    real_time_frame = tk.Frame(self.__window, width=1000, height=100)
    real_time_frame.pack(side=tk.TOP)
    self.real_time = RealTimeSwitch(real_time_frame, self.__c)
    self.real_time.draw(DEFAULT_REAL_TIME_ON)

    # ---- Main Panel ----
    main_panel_frame = tk.Frame(self.__window, width=1000, height=500)
    main_panel_frame.pack(side=tk.TOP)
    self.main_panel = MainPanel(main_panel_frame, self.__c)
    self.main_panel.draw(DEFAULT_REAL_TIME_ON)

    await self.__window.mainloop()

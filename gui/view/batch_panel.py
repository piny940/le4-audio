import tkinter as tk
from .voice_change_panel import VoiceChangePanel
from .view_base import ViewBase
from .file_select import FileSelect
from controller.interface import IController
from .slider import StartSlider, EndSlider
from .text_box import TextBox
from .control_panel import ControlPanel
from .play_button import PlayButton
from .stop_button import StopButton
from .reset_button import ResetButton
from .figures import Figures

class BatchPanel(ViewBase):
  def draw(self):
    # ----Figures ----
    spec_frame = tk.Frame(self._frame, width=1000, height=400)
    spec_frame.pack(side=tk.TOP)
    self.figures = Figures(spec_frame)

    # ---- File Select ----
    middle_buttons_frame = tk.Frame(self._frame, width=1000, height=100)
    middle_buttons_frame.pack(side=tk.TOP)
    self.file_select = FileSelect(middle_buttons_frame, self._c)
    self.file_select.draw()
    # ---- Play Button ----
    self.play_button = PlayButton(middle_buttons_frame, self._c)
    self.stop_button = StopButton(middle_buttons_frame, self._c)
    # ---- Reset Button ----
    self.reset_button = ResetButton(middle_buttons_frame, self._c)

    # ---- Start Slider ----
    start_slider_frame = tk.Frame(self._frame, width=1000, height=50)
    start_slider_frame.pack(side=tk.TOP)
    self.start_slider = StartSlider(start_slider_frame, self._c)

    # ---- End Slider ----
    end_slider_frame = tk.Frame(self._frame, width=1000, height=50)
    end_slider_frame.pack(side=tk.TOP)
    self.end_slider = EndSlider(end_slider_frame, self._c)

    # ---- Control Panel ----
    control_panel_frame = tk.Frame(
      self._frame,
      width=1000,
      height=380,
      padx=10,
      pady=10
    )
    control_panel_frame.pack(side=tk.TOP)
    self.control_panel = ControlPanel(control_panel_frame, self._c)

    self._set([
      spec_frame,
      middle_buttons_frame,
      start_slider_frame,
      end_slider_frame,
      control_panel_frame
    ])
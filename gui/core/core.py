import numpy as np


def is_peak(arr, index):
  if index == 0 or index == len(arr) - 1:
    return False
  return arr[index - 1] < arr[index] and arr[index] > arr[index + 1]


def get_f0(waveform, sampling_rate):
  autocorr = np.correlate(waveform, waveform, 'full')
  autocorr = autocorr[len(autocorr) // 2:]  # 不要な前半を捨てる

  # ピークを検出
  peak_indices = [i for i in range(len(autocorr)) if is_peak(autocorr, i)]
  peak_indices = [i for i in peak_indices if i != 0]  # 最初のピークは除く

  if len(peak_indices) == 0:
    return 0

  max_peak_index = max(peak_indices, key=lambda index: autocorr[index])

  # 基本周波数を推定
  f0 = sampling_rate / max_peak_index
  return f0


def get_f0s(waveform, sampling_rate, size_frame):
  f0s = []
  for i in np.arange(0, len(waveform) - size_frame, size_frame):
    idx = int(i)
    x_frame = waveform[idx: idx + size_frame]
    f0 = get_f0(x_frame, sampling_rate)
    f0s.append(f0)
  return f0s

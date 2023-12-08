import math
import numpy as np

CODES = [
    [0, 4, 7],
    [1, 5, 8],
    [2, 6, 9],
    [3, 7, 10],
    [4, 8, 11],
    [5, 9, 0],
    [6, 10, 1],
    [7, 11, 2],
    [8, 0, 3],
    [9, 1, 4],
    [10, 2, 5],
    [11, 3, 6],
    [0, 3, 7],
    [1, 4, 8],
    [2, 5, 9],
    [3, 6, 10],
    [4, 7, 11],
    [5, 8, 0],
    [6, 9, 1],
    [7, 10, 2],
    [8, 11, 3],
    [9, 0, 4],
    [10, 1, 5],
    [11, 2, 6]
]


def hz2nn(frequency):
  return int(round(12.0 * math.log(frequency / 440.0, 2) + 69))


def chroma_vector(spectrum):
  frequencies = np.linspace(8000 / len(spectrum), 8000, len(spectrum))

  # クロマベクトル
  cv = np.zeros(12)
  for s, f in zip(spectrum, frequencies):
    nn = hz2nn(f)
    cv[nn % 12] += math.abs(s)
  return cv


def spectrogram(waveform, size_frame, size_shift):
  spectrogram = []
  hamming_window = np.hamming(size_frame)

  for i in np.arange(0, len(waveform) - size_frame, size_shift):
    idx = int(i)
    x_frame = waveform[idx: idx + size_frame]

    # 窓掛けしたデータをFFT
    fft_spec = np.fft.rfft(x_frame * hamming_window)

    # 振幅スペクトルを対数化
    fft_log_abs_spec = np.log(np.abs(fft_spec))

    # 配列に保存
    spectrogram.append(fft_log_abs_spec)
  return spectrogram


def estimate_code(spectrum):
  cv = chroma_vector(spectrum)
  likelihoods = []
  for code in CODES:
    likelihood = 1.0 * cv[code[0]] + 0.5 * cv[code[1]] + 0.8 * cv[code[2]]
    likelihoods.append(likelihood)
  return np.argmax(likelihoods)

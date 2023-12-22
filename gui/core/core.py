import numpy as np
import librosa
from .constants import SR, SIZE_FRAME, NOTES
import math

def load_waveform(filename):
  x, _ = librosa.load(filename, sr=SR)
  return x


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

def hz2nn(frequency):
  return int(round(12.0 * math.log(frequency / 440.0, 2) + 69))

def nn2hz(nn):
  return 440.0 * 2 ** ((nn - 69) / 12.0)

def shs(spectrum, sample_rate, size_frame):
  likelihood = np.zeros(len(NOTES))
  for i in range(len(likelihood)):
    base_freq = nn2hz(NOTES[i])
    for j in range(1, 16):
      freq = base_freq * j
      fft_idx = int(freq * size_frame / sample_rate)
      likelihood[i] += 0.8**j * np.exp(spectrum[fft_idx])
  return NOTES[np.argmax(likelihood)]


def get_melody(spectrogram):
  melody = []
  for spectrum in spectrogram:
    melody.append(shs(spectrum, SR, SIZE_FRAME))
  return melody

def generate_sinusoid(sampling_rate, frequency, duration):
  sampling_interval = 1.0 / sampling_rate
  t = np.arange(sampling_rate * duration) * sampling_interval
  waveform = np.sin(2.0 * math.pi * frequency * t)
  return waveform

def voice_change(waveform, sampling_rate, frequency):
  duration = len(waveform)
  sin_wave = generate_sinusoid(sampling_rate, frequency, duration / sampling_rate)
  sin_wave = sin_wave * 0.9
  return waveform * sin_wave

def tremolo(waveform, sampling_rate, frequency, depth):
  tremolo_waveform = generate_sinusoid(sampling_rate, frequency, len(waveform) / sampling_rate)
  changed = waveform * (1.0 + depth * tremolo_waveform)
  return changed / np.max(np.abs(changed))

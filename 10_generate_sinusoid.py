import sys
import math
import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt


def generate_sinusoid(sampling_rate, frequency, duration):
  sampling_interval = 1.0 / sampling_rate
  t = np.arange(sampling_rate * duration) * sampling_interval
  waveform = np.sin(2.0 * math.pi * frequency * t)
  return waveform


def write_waveform(filename, waveform, sampling_rate):
  waveform = waveform * 0.9 / np.max(waveform)  # 最大値を0.9にする
  waveform = (waveform * 32768.0).astype('int16')
  scipy.io.wavfile.write(filename, int(sampling_rate), waveform)


SAMPLING_RATE = 16000.0
DURATION = 2.0  # 生成する正弦波の時間的長さ

FIRST_FREC = 440
SECOND_FREC = 880

waveform = generate_sinusoid(SAMPLING_RATE, SECOND_FREC, DURATION)
write_waveform(f'audio/sinusoid{SECOND_FREC}.wav', waveform, SAMPLING_RATE)

waveform += generate_sinusoid(SAMPLING_RATE, FIRST_FREC, DURATION)
write_waveform(f'audio/sinusoid{FIRST_FREC}_{SECOND_FREC}.wav', waveform, SAMPLING_RATE)

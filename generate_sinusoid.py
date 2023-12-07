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


SAMPLING_RATE = 16000.0
FREQUENCY = 440.0
DURATION = 2.0  # 生成する正弦波の時間的長さ

waveform = generate_sinusoid(SAMPLING_RATE, FREQUENCY, DURATION)

waveform = waveform * 0.9  # 最大値を0.9にする

waveform = (waveform * 32768.0).astype('int16')

fig = plt.figure()
plt.plot(waveform[0:100])
plt.show()

filename = 'audio/sinusoid440.wav'
scipy.io.wavfile.write(filename, int(SAMPLING_RATE), waveform)

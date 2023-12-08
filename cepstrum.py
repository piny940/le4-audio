import matplotlib.pyplot as plt
import numpy as np
import librosa


def get_log_spec(x_frame):
  spec = np.fft.rfft(x_frame)
  log_spec = np.log(np.abs(spec))
  return log_spec


def get_cepstrum(x_frame):
  spec = np.fft.rfft(x_frame)
  log_spec = np.log(np.abs(spec))
  cepstrum = np.fft.rfft(log_spec)
  return cepstrum


def show(filename, log_spec, cepstrum):
  fig = plt.figure()

  plt.xlabel('frequency [Hz]')
  plt.ylabel('amplitude')

  x_data = np.linspace((SR / 2) / len(log_spec), SR / 2, len(log_spec))
  plt.plot(x_data, log_spec)
  plt.plot(x_data, cepstrum)

  plt.show()
  fig.savefig(filename)


SR = 16000

x_long, _ = librosa.load('audio/aiueo-long.wav', sr=SR)
a_long = x_long[8000:16000]
i_long = x_long[26000:40000]
u_long = x_long[55000:65000]
e_long = x_long[80000:85000]
o_long = x_long[98000:105000]

x_short, _ = librosa.load('audio/aiueo-short.wav', sr=SR)
a_short = x_short[10000:12000]
i_short = x_short[23000:25000]
u_short = x_short[38000:40000]
e_short = x_short[52000:54000]
o_short = x_short[63000:65000]

data = [
    [x_long, 'full_long'],
    [a_long, 'a_long'],
    [i_long, 'i_long'],
    [u_long, 'u_long'],
    [e_long, 'e_long'],
    [o_long, 'o_long'],
    [x_short, 'full_short'],
    [a_short, 'a_short'],
    [i_short, 'i_short'],
    [u_short, 'u_short'],
    [e_short, 'e_short'],
    [o_short, 'o_short'],
]

LEVEL = 13

for x, label in data:
  spec = get_log_spec(x)
  x_data = np.linspace((SR / 2) / len(spec), SR / 2, len(spec))

  cepstrum = get_cepstrum(x)
  low_cepstrum = cepstrum[:LEVEL]
  r = np.fft.irfft(low_cepstrum, n=len(x_data))

  fig = plt.figure()

  plt.xlabel('frequency [Hz]')
  plt.ylabel('amplitude')

  plt.plot(x_data, spec)
  plt.plot(x_data, r)

  plt.show()
  fig.savefig(f'plot/envelope/{label}.png')

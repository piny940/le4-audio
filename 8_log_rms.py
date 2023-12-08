import matplotlib.pyplot as plt
import numpy as np
import librosa

SR = 16000


def show_volume(filename, output):
  x_long, _ = librosa.load(filename, sr=SR)

  frame_size = 128

  rms_long = []
  for i in np.arange(0, len(x_long) - frame_size, frame_size):
    idx = int(i)
    x_frame = x_long[idx: idx + frame_size]
    rms_long.append(np.sqrt(np.mean(x_frame ** 2)))

  volume_long = 20 * np.log10(rms_long)
  print(volume_long)
  fig = plt.figure(figsize=(10, 4))

  plt.xlabel('Sampling point')

  plt.plot(volume_long)
  plt.show()

  fig.savefig(output)


show_volume('audio/aiueo-long.wav', 'plot/volume-long.png')
show_volume('audio/aiueo-short.wav', 'plot/volume-short.png')

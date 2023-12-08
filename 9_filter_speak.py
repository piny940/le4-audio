import matplotlib.pyplot as plt
import numpy as np
import librosa


def get_volumes(x, frame_size):
  rms = []
  for i in np.arange(0, len(x) - frame_size, frame_size):
    idx = int(i)
    x_frame = x[idx: idx + frame_size]
    rms.append(np.sqrt(np.mean(x_frame ** 2)))

  volume = 20 * np.log10(rms)
  return volume


SR = 16000
FRAME_SIZE = 128
THRESHOLD = -20

x, _ = librosa.load('audio/aiueo-long.wav', sr=SR)
volumes = get_volumes(x, FRAME_SIZE)

is_speaking = False
for i, volume in enumerate(volumes):
  if is_speaking and volume < THRESHOLD:
    is_speaking = False
    print(f'end: {i * FRAME_SIZE / SR} s')
  elif not is_speaking and volume >= THRESHOLD:
    is_speaking = True
    print(f'start: {i * FRAME_SIZE / SR} s')

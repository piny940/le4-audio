import matplotlib.pyplot as plt
import numpy as np
import librosa

SR = 16000

x, _ = librosa.load('audio/aiueo-long.wav', sr=SR)

fft_spec = np.fft.rfft(x)

fft_log_abs_spec = np.log(np.abs(fft_spec))

fig = plt.figure()

plt.xlabel('frequency [Hz]')
plt.ylabel('amplitude')

x_data = np.linspace((SR / 2) / len(fft_log_abs_spec), SR / 2, len(fft_log_abs_spec))
plt.plot(x_data, fft_log_abs_spec)

plt.show()
fig.savefig('plot/rfft.png')

fig = plt.figure()
plt.xlabel('frequency [Hz]')
plt.ylabel('amplitude')
plt.xlim(0, 2000)
plt.plot(x_data, fft_log_abs_spec)

plt.show()

fig.savefig('plot/rfft_2k.png')

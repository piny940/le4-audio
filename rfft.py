import matplotlib.pyplot as plt
import numpy as np
import librosa

SR = 16000

x, _ = librosa.load('audio/aiueo-long.wav', sr=SR)

# 入力: 波を表す1次元配列。時間を横軸として、サンプリング周波数ごとの波の振幅をプロットする。
# 出力: フーリエ変換後の値。周波数を横軸として、各周波数ごとの離散フーリエ変換の出力値をプロットする。
fft_spec = np.fft.rfft(x)
a_fft = np.fft.rfft(x[8000:16000])
i_fft = np.fft.rfft(x[26000:40000])
u_fft = np.fft.rfft(x[55000:65000])
e_fft = np.fft.rfft(x[80000:85000])
o_fft = np.fft.rfft(x[98000:105000])

fft_log_abs_spec = np.log(np.abs(fft_spec))
a_fft_log_abs = np.log(np.abs(a_fft))
i_fft_log_abs = np.log(np.abs(i_fft))
u_fft_log_abs = np.log(np.abs(u_fft))
e_fft_log_abs = np.log(np.abs(e_fft))
o_fft_log_abs = np.log(np.abs(o_fft))

filenames = ['full', 'a', 'i', 'u', 'e', 'o']

for i, spec in enumerate([fft_log_abs_spec, a_fft_log_abs, i_fft_log_abs, u_fft_log_abs, e_fft_log_abs, o_fft_log_abs]):
  fig = plt.figure()

  plt.xlabel('frequency [Hz]')
  plt.ylabel('amplitude')

  x_data = np.linspace((SR / 2) / len(spec), SR / 2, len(spec))
  plt.plot(x_data, spec)

  plt.show()
  fig.savefig(f'plot/rfft/{filenames[i]}.png')

  fig = plt.figure()
  plt.xlabel('frequency [Hz]')
  plt.ylabel('amplitude')
  plt.xlim(0, 2000)
  plt.plot(x_data, spec)

  plt.show()

  fig.savefig(f'plot/rfft/{filenames[i]}-2k.png')

import numpy as np
import librosa
import matplotlib.pyplot as plt


def get_spec(x_frame):
  spec = np.fft.rfft(x_frame)
  log_spec = np.log(np.abs(spec))
  return log_spec


def get_cepstrum(x_frame):
  spec = get_spec(x_frame)
  cepstrum = np.fft.rfft(spec)
  log_cepstrum = np.log(np.abs(cepstrum))
  return log_cepstrum  # 横軸をfreqとする一次元配列


def get_cepstrums(waveform, size_frame):
  # waveform: 波を表す一次元配列
  cepstrums = np.array([])
  length1 = 0
  for i in np.arange(0, len(waveform) - size_frame, size_frame):
    idx = int(i)
    x_frame = waveform[idx: idx + size_frame]
    cepstrum = get_cepstrum(x_frame)
    cepstrums = np.append(cepstrums, cepstrum)
    length1 += 1
    length2 = len(cepstrum)
  cepstrums = cepstrums.reshape(length1, length2)
  return cepstrums  # 二次元配列


def zero_cross(waveform):
  d = np.array(waveform)
  return sum([1 if x < 0.0 else 0 for x in d[1:] * d[:-1]])


def zero_cross_rate(waveform, sample_rate):
  # 単位時間あたりのゼロクロス数
  return zero_cross(waveform) / (len(waveform) / sample_rate)


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


def is_voiced_sound(waveform, sampling_rate):
  f0 = get_f0(waveform, sampling_rate)
  zcr = zero_cross_rate(waveform, sampling_rate)
  if f0 == 0:
    return False
  rate = zcr / f0
  return 1.95 < rate < 6.0


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


def learn_avg(arr):
  return np.average(arr, axis=0)


def learn_var(arr, avg):
  return np.average((arr - avg) ** 2, axis=0)


def likelihood(x, avg, var):
  return - np.sum((x - avg) ** 2 / var / 2 + np.log(var))


def predict(x, avgs, vars):
  ans = None
  max_likelihood = - np.inf
  for i, (avg, var) in enumerate(zip(avgs, vars)):
    cepstrums = get_cepstrum(x)
    like = likelihood(cepstrums, avg, var)
    if like > max_likelihood:
      max_likelihood = like
      ans = i
  return ans


def recognize(waveform, avgs, vars, size_frame):
  # waveformを短いフレームに分割して、それぞれのフレームがどの音素に属するかを調べる
  recognized = np.array([])
  for i in np.arange(0, len(waveform) - size_frame, size_frame):
    idx = int(i)
    x_frame = waveform[idx: idx + size_frame]
    pred = predict(x_frame, avgs, vars)
    recognized = np.append(recognized, pred)
  return recognized


SR = 16000

x_long, _ = librosa.load('audio/aiueo-long.wav', sr=SR)
a = x_long[8000:16000]
i = x_long[26000:40000]
u = x_long[55000:65000]
e = x_long[80000:85000]
o = x_long[98000:105000]
learn_data = [a, i, u, e, o]

SIZE_FRAME = 512

avgs = []
vars = []
for data in learn_data:
  cepstrums = get_cepstrums(data, SIZE_FRAME)
  # print(cepstrums)
  avg = learn_avg(cepstrums)
  var = learn_var(cepstrums, avg)
  avgs.append(avg)
  vars.append(var)

# シフトサイズ
SHIFT_SIZE = 16000 / 100  # 10 msec

x_short, _ = librosa.load('audio/aiueo-short.wav', sr=SR)

spec = spectrogram(x_short, SIZE_FRAME, SHIFT_SIZE)
rec = recognize(x_short, avgs, vars, SIZE_FRAME)

fig = plt.figure()

plt.xlabel('sample')
plt.ylabel('frequency [Hz]')

plt.plot(np.linspace(0, len(x_short), len(rec)), rec * 500)

plt.imshow(
    np.flipud(np.array(spec).T),
    extent=[0, len(x_short), 0, SR / 2],
    aspect='auto',
    interpolation='nearest'
)
plt.ylim(0, 2000)

plt.show()
fig.savefig('plot/recognition/aiueo-short.png')

import math
import numpy as np
import librosa
import matplotlib.pyplot as plt

NOTES = range(36, 60)


def hz2nn(frequency):
  return int(round(12.0 * math.log(frequency / 440.0, 2) + 69))


def nn2hz(nn):
  return 440.0 * 2 ** ((nn - 69) / 12.0)


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


def shs(spectrum, sample_rate, size_frame):
  likelihood = np.zeros(len(NOTES))
  for idx, spec in enumerate(spectrum):
    if idx == 0:
      continue
    freq = idx * sample_rate / size_frame
    if hz2nn(freq) not in NOTES:
      continue
    nn = hz2nn(freq)
    likelihood[nn - NOTES[0]] += spec
  return NOTES[np.argmax(likelihood)]


def get_melody(spectrogram):
  melody = []
  for spectrum in spectrogram:
    melody.append(shs(spectrum, SR, SIZE_FRAME))
  return melody


SR = 16000
SIZE_FRAME = 2048
SHIFT_SIZE = 16000 / 100  # 10 msec
# https://www.youtube.com/watch?v=Ci_zad39Uhw
x, _ = librosa.load('audio/shs-test-man.wav', sr=SR)

spec = spectrogram(x, SIZE_FRAME, SHIFT_SIZE)
melody = get_melody(spec)

fig = plt.figure()

plt.plot(x)
plt.xlabel('sample')
# plt.show()

fig.savefig('plot/melody/sts-test.wave.png')

fig = plt.figure()

plt.xlabel('sample')
plt.ylabel('frequency [Hz]')
plt.imshow(
    np.flipud(np.array(spec).T),
    extent=[0, len(x), 0, SR / 2],
    aspect='auto',
    interpolation='nearest'
)
# plt.show()

fig.savefig('plot/melody/sts-test.spectrogram.png')

fig = plt.figure()
plt.xlabel('sample')
plt.ylabel('frequency [Hz]')

plt.plot(np.linspace(0, len(x), len(melody)), list(map(lambda x: x - NOTES[0], melody)))
plt.yticks(np.arange(24),
           list(["A3", "A#3", "B3", "C4", "C#4", "D4", "D#4", "E4",
                 "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5",
                 "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5"]))

plt.show()
fig.savefig('plot/melody/sts-test.melody.png')

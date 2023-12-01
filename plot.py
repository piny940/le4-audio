import matplotlib.pyplot as plt
import librosa

SR = 16000

x, _ = librosa.load('audio/aiueo-long.wav', sr=SR)

print(x)
fig = plt.figure(figsize=(10, 4))

plt.plot(x)
plt.xlabel('Sampling_point')
plt.show()

fig.savefig('plot/aiueo.png')

import numpy as np

# サンプリングレート
SAMPLING_RATE = 16000

# フレームサイズ
FRAME_SIZE = 2048

# サイズシフト
SHIFT_SIZE = int(SAMPLING_RATE / 20)	# 今回は0.05秒

# スペクトルをカラー表示する際に色の範囲を正規化するために
# スペクトルの最小値と最大値を指定
# スペクトルの値がこの範囲を超えると，同じ色になってしまう
SPECTRUM_MIN = -5
SPECTRUM_MAX = 1

# 音量を表示する際の値の範囲
VOLUME_MIN = -120
VOLUME_MAX = -10

# log10を計算する際に，引数が0にならないようにするためにこの値を足す
EPSILON = 1e-10

# ハミング窓
hamming_window = np.hamming(FRAME_SIZE)

# グラフに表示する縦軸方向のデータ数
MAX_NUM_SPECTROGRAM = int(FRAME_SIZE / 2)

# グラフに表示する横軸方向のデータ数
NUM_DATA_SHOWN = 100

NOTES = range(36, 60)

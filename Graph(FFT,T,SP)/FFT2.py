import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

dataset = pd.read_csv("../emgraw.csv")
num_channels = 8
num_gesture = 6
n = len(dataset)
Fs = 1000
num_rows = 2
num_columns = 3
fig, axes = plt.subplots(num_rows, num_columns, figsize=(14, 8))

for p in range(num_gesture):
    row = p // num_columns
    col = p % num_columns
    for i in range(num_channels):
        fft_result = np.fft.fft((pd.DataFrame(dataset.iloc[1500*p+500:1600*p+1600, i+1])))
        n = len(fft_result)
        frequencies = np.fft.fftfreq(n, 1 / Fs)
        axes[row, col].plot(frequencies, np.abs(fft_result), label=f'Channel {i+1}')
        axes[row, col].set_title(f'Gesture {p + 1}', fontsize=10)
        axes[row, col].set_xlabel('Frequency')
        axes[row, col].set_ylabel('Magnitude')
        axes[row, col].grid(True)
        axes[row, col].set_xlim(0, 500)
for i in range(num_channels, num_rows * num_columns):
    fig.delaxes(axes[i])

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Set rect to adjust the main title's position
plt.show()

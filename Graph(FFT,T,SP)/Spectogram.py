import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import spectrogram
from scipy import signal

dataset = pd.read_csv("../emgraw.csv")
Fs = 1000
num_rows = 2
num_columns = 3
fig, axes = plt.subplots(num_rows, num_columns, figsize=(14, 8))
num_gesture = 6
num_channels = 8
nperseg = 256
noverlap = 128

for p in range(num_gesture):
    row = p // num_columns
    col = p % num_columns
    for i in range(num_channels):
        frequencies, times, Sxx = spectrogram((dataset.iloc[1500*p+500:1600*p+1600, i+1]), fs=Fs, nperseg=nperseg, noverlap=noverlap)
        im = axes[row, col].pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='auto', cmap='bone')
        axes[row, col].set_title(f'Gesture {p + 1}', fontsize=10)
        axes[row, col].set_xlabel('Time (s)')
        axes[row, col].set_ylabel('Frequency (Hz)')
        axes[row, col].grid(True)

cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])  # Adjust the position and size as needed

cbar = fig.colorbar(im, cax=cbar_ax, label='Power/Frequency (dB/Hz)')
for gesture in range(num_gesture, num_rows * num_columns):
    fig.delaxes(axes.flatten()[gesture])

#for i in range(num_channels, num_rows * num_columns):
    #fig.delaxes(axes[i])

plt.tight_layout(rect=[0, 0.03, 0.9, 0.95])
plt.show()
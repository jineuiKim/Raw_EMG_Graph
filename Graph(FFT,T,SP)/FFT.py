import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("../raw_EMG.csv")
num_channels = 8
n = len(dataset)
Fs = 1000
frequencies = np.fft.fftfreq(n, 1/Fs)
num_rows = 2
num_columns = 4
fig, axes = plt.subplots(num_rows, num_columns, figsize=(14, 8))

for i in range(num_channels):
    row = i // num_columns  # Calculate the row index
    col = i % num_columns   # Calculate the column index
    fft_result = np.fft.fft(pd.DataFrame(dataset.iloc[:, i + 1]))
    axes[row, col].plot(frequencies, np.abs(fft_result))
    axes[row, col].set_title(f'Channel {i + 1}', fontsize=10)
    axes[row, col].set_xlabel('Frequency')
    axes[row, col].set_ylabel('Magnitude')
    axes[row, col].grid(True)
    axes[row, col].set_xlim(0, 500)

for i in range(num_channels, num_rows * num_columns):
    fig.delaxes(axes[i])

# Adjust subplot layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Set rect to adjust the main title's position
plt.show()
###제스쳐별로 해야댐


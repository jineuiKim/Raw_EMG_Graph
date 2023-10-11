import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your EMG data from a CSV file
dataset = pd.read_csv("../emgraw.csv")
result = pd.DataFrame()

# Number of channels (assuming 8 channels)
num_channels = 8
plt.figure(figsize=(12, 12))
# Extract the EMG data into a NumPy array
for i in range(num_channels):
    plt.subplot(2, 4, i + 1)
    emg_data = dataset.iloc[4400:5300, i+1].values * 1000
    image_data = emg_data.reshape(30, 30)
    plt.imshow(image_data, cmap='viridis', interpolation='gaussian', aspect='auto')


print(emg_data)
# Transpose the data so that rows correspond to channels and columns correspond to time


plt.tight_layout()
plt.colorbar(label='EMG Intensity')
plt.grid(False)
plt.show()
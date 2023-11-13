import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
import seaborn as sns

dataset = []                             # Declare an empty list named mylines.
with open ('test.txt', 'rt') as myfile: # Open lorem.txt for reading text data.
    for data in myfile:                # For each line, stored as myline,
        dataset.append(data)

data = pd.DataFrame([line.split() for line in dataset])

# Set the first row as column headers (if applicable)
data.columns = data.iloc[0]
data = data[1:]
fs = 250
num_channels = 5
## 8952 ~ 9110

####fist#####
for i in num_channels():
    channel_data = data.iloc[8925:9110, i+1]
    f, Pxx = welch(channel_data, fs, nperseg= 1024)
    band_start = 5
    band_end = 15
    band_indices = np.where 


# Finding the indices corresponding to the defined frequency band
band_indices = np.where((f >= band_start) & (f <= band_end))

# Calculate bandpower as the average power in the defined frequency band
bandpower = np.mean(Pxx[band_indices])

print("Bandpower of the EMG signal in the frequency band {} to {} Hz: {:.4f}".format(band_start, band_end, bandpower))
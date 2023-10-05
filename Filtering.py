import numpy as np

import pandas as pd

# Define filter parameters (adjust as needed)
lowcut = 20.0  # Lower cutoff frequency in Hz
highcut = 500.0  # Upper cutoff frequency in Hz
fs = 1000.0  # Sampling frequency in Hz

dataset = pd.read_csv("emgraw.csv")
x = pd.DataFrame(dataset.iloc[:,1:-1])
y = dataset.iloc[:,-1].values

# Function to apply a bandpass filter to each channel
def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data, axis=0)
    return y
print(x.columns)

for column in x.columns:
    filtered_channels[column]: butter_bandpass_filter()